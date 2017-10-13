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


def information_list(request):
    """
    根据不同的公司，产品，事件选项得到排序后的新闻对象列表
    :param request:
    :return:
    """
    company_id = request.POST.get("company_id", 2)
    # product_id = request.POST.get("product_id", 2)
    # event_id = request.POST.get("event_id", 2)
    start_time = request.POST.get("start_time", common.default_start_time)
    end_time = request.POST.get("end_time", common.default_end_time)
    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    get_sort_news_objects_list = mongo_data.get_sort_news_objects_list(data_source_id_list,
                                                                       paras=settings.MONGO_PARA,
                                                                       start_time=start_time,
                                                                       end_time=end_time)
    contents = {"get_sort_news_objects_list": get_sort_news_objects_list}
    return JsonResponse(contents)


def information_detail(request):
    """
    根据资讯的id得到资讯的详细信息
    :param request:
    :return:
    """
    media_source = request.POST.get("media_source", "baidu_tieba")
    information_id = request.POST.get("information_id", "59dc7724286fd49c3ed77ed6")

    contents = {}
    source_media_instance_dict = mongo_data.get_source_media_instance_dict(paras=settings.MONGO_PARA)
    information_obj = source_media_instance_dict[media_source].get_object(ObjectId(information_id))

    if media_source == "weibo":
        weibo_id = [obj.get("weibo_id") for obj in information_obj][0]
        weibo_comment_obj = source_media_instance_dict[media_source].get_comment_obj(weibo_id).limit(5)
        weibo_comment_obj_list = [common.serialize_news_obj(obj) for obj in weibo_comment_obj]
        contents["weibo_comment_obj_list"] = weibo_comment_obj_list

    if media_source == "baidu_zhidao":
        url = [obj.get("url") for obj in information_obj][0]
        reply_obj = source_media_instance_dict[media_source].get_reply_obj(url)
        reply_obj_list = [common.serialize_news_obj(obj) for obj in reply_obj]
        if len(reply_obj_list) > 0:
            reply_obj_list.sort(key=lambda x: x["answer_like_count"], reverse=True)
            contents["reply_obj"] = reply_obj_list[:5]
        else:
            contents["reply_obj"] = []

    if media_source == "zhihu":
        pass

    if media_source == "baidu_tieba":
        # url = [obj.get("url") for obj in information_obj][0]
        url = "http://tieba.baidu.com/p/5152644693?pid=107902501395&cid=0"
        reply_obj = source_media_instance_dict[media_source].get_reply_obj(url)
        reply_obj_list = [common.serialize_news_obj(obj) for obj in reply_obj if obj.get("building_no") > 1]

        if len(reply_obj_list) > 0:
            reply_obj_list.sort(key=lambda x: x["building_no"])
            contents["reply_obj"] = reply_obj_list[:5]
        else:
            contents["reply_obj"] = []

    serialize_information_obj = common.serialize_news_obj(information_obj.clone())
    contents["information_obj"] = serialize_information_obj

    return JsonResponse(contents)
