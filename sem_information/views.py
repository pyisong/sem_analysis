# -*- coding:utf-8 -*-
# from django.shortcuts import render
# import logging
from common import mysql_data, mongo_data, settings, common
from django.http import JsonResponse
from bson import ObjectId
# Create your views here.

# logger = logging.getLogger(__name__)
# logger.info(__name__)
# logger.error(__name__)


def inform_list(request):
    """
    根据不同的公司，产品，事件选项得到排序后的新闻对象列表
    :param request:
    :return:
    """
    comp_id = request.POST.get("comp_id", 2)
    # product_id = request.POST.get("product_id", 2)
    # event_id = request.POST.get("event_id", 2)
    start_time = request.POST.get("start_time", common.default_start_time)
    end_time = request.POST.get("end_time", common.default_end_time)
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(comp_id))
    get_sort_news_objs_list = mongo_data.get_sort_news_objs_list(data_sour_id_list,
                                                                 paras=settings.MONGO_PARA,
                                                                 start_time=start_time,
                                                                 end_time=end_time)
    contents = {"get_sort_news_objs_list": get_sort_news_objs_list}
    return JsonResponse(contents)


def inform_det(request):
    """
    根据资讯的id得到资讯的详细信息
    :param request:
    :return:
    """
    med_sour = request.POST.get("med_sour", "baidu_tieba")
    inform_id = request.POST.get("inform_id", "59dc7724286fd49c3ed77ed6")

    contents = {}
    sour_med_ins_dict = mongo_data.get_sour_med_ins_dict(paras=settings.MONGO_PARA)
    inform_obj = sour_med_ins_dict[med_sour].get_object(ObjectId(inform_id))

    if med_sour == "weibo":
        weibo_id = [obj.get("weibo_id") for obj in inform_obj][0]
        weibo_comt_obj = sour_med_ins_dict[med_sour].get_comt_obj(weibo_id).limit(5)
        weibo_comt_obj_list = [common.seria_news_obj(obj) for obj in weibo_comt_obj]
        contents["weibo_comt_obj_list"] = weibo_comt_obj_list

    if med_sour == "baidu_zhidao":
        url = [obj.get("url") for obj in inform_obj][0]
        reply_obj = sour_med_ins_dict[med_sour].get_reply_obj(url)
        reply_obj_list = [common.seria_news_obj(obj) for obj in reply_obj]
        if len(reply_obj_list) > 0:
            reply_obj_list.sort(key=lambda x: x["answer_like_count"], reverse=True)
            contents["reply_obj"] = reply_obj_list[:5]
        else:
            contents["reply_obj"] = []

    if med_sour == "zhihu":
        pass

    if med_sour == "baidu_tieba":
        # url = [obj.get("url") for obj in inform_obj][0]
        url = "http://tieba.baidu.com/p/5152644693?pid=107902501395&cid=0"
        reply_obj = sour_med_ins_dict[med_sour].get_reply_obj(url)
        reply_obj_list = [common.seria_news_obj(obj) for obj in reply_obj if obj.get("building_no") > 1]

        if len(reply_obj_list) > 0:
            reply_obj_list.sort(key=lambda x: x["building_no"])
            contents["reply_obj"] = reply_obj_list[:5]
        else:
            contents["reply_obj"] = []

    seria_inform_obj = common.seria_news_obj(inform_obj.clone())
    contents["inform_obj"] = seria_inform_obj

    return JsonResponse(contents)
