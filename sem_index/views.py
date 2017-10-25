# -*- coding:utf-8 -*-
# from django.forms import model_to_dict
# from django.shortcuts import render
import traceback
# import logging
from django.http import JsonResponse
from common import mongo_data, common, source_media, mysql_data, settings
# Create your views here.

# logger = logging.getLogger("django")  # 这里用__name__通用,自动检测.
# logger.info(__name__)
# logger.error(__name__)


def infl_show(request, company_id):
    """
    影响力对比展示
    :param company_id:
    :param request:
    :return:
    """
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(company_id))
    contents = mongo_data.get_tal_infl_chg(data_sour_id_list, paras=settings.MONGO_PARA)
    return JsonResponse(contents)


def search_exponent(request):
    """
    搜索曲线
    :param request:
    :return:
    """
    pass


def infl_dire(request, company_id):
    """
    影响力导向
    :param request:
    :param company_id:
    :return:
    """
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(company_id))
    sent_infl_dict = mongo_data.get_sent_infl(data_sour_id_list, paras=settings.MONGO_PARA)
    contents = sent_infl_dict
    return JsonResponse(contents)


def tod_sem(request, company_id):
    """
    今日舆情(最近7天的分别列出不同数据源的不同情感的影响力)
    :param request:
    :param company_id:
    :return:
    """
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(company_id))
    sour_med_ins_dict = mongo_data.get_sour_med_ins_dict(paras=settings.MONGO_PARA)
    contents = {}
    for key in sour_med_ins_dict:
        sent_stas = sour_med_ins_dict[key].get_sent_stas(
            data_sour_id_list=data_sour_id_list,
            start_time=common.default_start_time,
            end_time=common.default_end_time
        )
        contents[key] = {"negative": 0, "positive": 0, "neutral": 0}
        for item in sent_stas:
            # 'negative', 'positive', 'neutral'
            contents[key][item.get("_id")] += item.get("count")
    return JsonResponse(contents)


def tod_hot(request, company_id):
    """
    今日热点
    :param request:
    :param company_id:
    :return:
    """
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(company_id))
    tod_hot_dict = {}
    sour_med_ins_dict = mongo_data.get_sour_med_ins_dict(paras=settings.MONGO_PARA)
    for key, value in sour_med_ins_dict.items():
        try:
            result = value.get_sort_news_objs(data_sour_id_list)["tod_sort_news_objs"].clone()[:1]
            tod_hot_dict[key] = common.seria_news_obj(result)
        except IndexError:
            print (traceback.print_exc())
    return JsonResponse(tod_hot_dict)


def tod_inform(request, company_id):
    """
    资讯
    :param request:
    :param company_id:
    :return:
    """
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(company_id))
    tod_dif_inform_list = []
    sour_med_ins_dict = mongo_data.get_sour_med_ins_dict(paras=settings.MONGO_PARA)
    for key in ["baidu_search", "weixin", "zhihu"]:
        tod_dif_inform_list.append(
            sour_med_ins_dict[key].get_sort_news_objs(
                data_sour_id_list)["tod_sort_news_objs"].clone().limit(10))
    inform_list = common.sort_dif_data_sour_obj(tod_dif_inform_list)[:10]
    contents = {"inform": inform_list}
    return JsonResponse(contents)


def weibo(request, company_id):
    """
    微博
    :param request:
    :param company_id:
    :return:
    """
    # data_sour_id_list = mysql_data.get_data_sour_id_list(int(company_id))
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(company_id))

    if len(data_sour_id_list) > 0:
        weibo_ins = mongo_data.get_sour_med_ins_dict(settings.MONGO_PARA)["weibo"]
        weibo_obj = \
            weibo_ins.get_sort_news_objs(data_sour_id_list)["tod_sort_news_objs"].clone().limit(10)
        # 对weibo_obj进行序列化
        weibo_obj_list = common.seria_news_obj(weibo_obj)
        contents = {"weibo_obj": weibo_obj_list}
    else:
        contents = {}
    return JsonResponse(contents)


def baidu_zhidao(request, company_id):
    """
    百度知道
    :param request:
    :param company_id:
    :return:
    """
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(company_id))
    sour_med_ins_dict = mongo_data.get_sour_med_ins_dict(paras=settings.MONGO_PARA)
    zhidao_tieba_list = []
    for key in ["baidu_zhidao", "baidu_tieba"]:
        zhidao_tieba_list.append(
            sour_med_ins_dict[key].get_sort_news_objs(
                data_sour_id_list)["tod_sort_news_objs"].clone().limit(10))
    zhidao_tieba_sort_list = common.sort_dif_data_sour_obj(zhidao_tieba_list)[:10]
    contents = {"baidu_zhidao_tieba": zhidao_tieba_sort_list}
    return JsonResponse(contents)


def app_info(request, company_id):
    """
    APP应用信息
    :param request:
    :param company_id:
    :return:
    """
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(company_id))
    app_store_ins = source_media.AppStore(paras=settings.MONGO_PARA)
    app_bd_info = app_store_ins.get_app_bd_info_obj(data_sour_id_list)
    app_comts_info = app_store_ins.get_app_comts_info(data_sour_id_list)
    # app_detail = app_store_ins.get_app_detail_obj(data_sour_id_list)
    contents = {
        "app_bd_info": app_bd_info,
        "sent_count_dict": app_comts_info["sent_count_dict"],
        "rating_count_dict": app_comts_info["rating_count_dict"],
                }

    return JsonResponse(contents)
