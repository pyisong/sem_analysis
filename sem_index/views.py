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


def influence_show(request, company_id):
    """
    影响力对比展示
    :param company_id:
    :param request:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    total_influence_dict = mongo_data.get_total_influence(data_source_id_list, paras=settings.MONGO_PARA)
    total_influence_change_dict = mongo_data.get_total_influence_change(data_source_id_list,
                                                                        paras=settings.MONGO_PARA)
    contents = total_influence_dict.copy()
    contents.update(total_influence_change_dict)
    # contents = dict(total_influence_dict.items() + total_influence_change_dict.items())
    return JsonResponse(contents)


def search_exponent(request):
    """
    搜索曲线
    :param request:
    :return:
    """
    pass


def influence_directive(request, company_id):
    """
    影响力导向
    :param request:
    :param company_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    sentiment_influence_dict = mongo_data.get_sentiment_influence(data_source_id_list,
                                                                  paras=settings.MONGO_PARA)
    contents = sentiment_influence_dict
    return JsonResponse(contents)


def today_sem(request, company_id):
    """
    今日舆情(最近7天的分别列出不同数据源的不同情感的影响力)
    :param request:
    :param company_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    source_media_instance_dict = mongo_data.get_source_media_instance_dict(paras=settings.MONGO_PARA)
    contents = {}
    for key in source_media_instance_dict:
        contents[key] = \
            source_media_instance_dict[key].get_sentiment_influence(
                data_source_id_list)["seven_sentiment_influence_dict"]
    return JsonResponse(contents)


def today_hot(request, company_id):
    """
    今日热点
    :param request:
    :param company_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    today_hot_dict = {}
    source_media_instance_dict = mongo_data.get_source_media_instance_dict(paras=settings.MONGO_PARA)
    for key, value in source_media_instance_dict.items():
        try:
            result = value.get_sort_news_objects(data_source_id_list)["today_sort_news_objects"].clone()[:1]
            today_hot_dict[key] = common.serialize_news_obj(result)
        except IndexError:
            print (traceback.print_exc())
    return JsonResponse(today_hot_dict)


def today_information(request, company_id):
    """
    资讯
    :param request:
    :param company_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    today_dif_information_list = []
    source_media_instance_dict = mongo_data.get_source_media_instance_dict(paras=settings.MONGO_PARA)
    for key in ["baidu_search", "weixin", "zhihu"]:
        today_dif_information_list.append(
            source_media_instance_dict[key].get_sort_news_objects(
                data_source_id_list)["today_sort_news_objects"].clone().limit(10))
    information_list = common.sort_dif_data_source_obj(today_dif_information_list)[:10]
    contents = {"information": information_list}
    return JsonResponse(contents)


def weibo(request, company_id):
    """
    微博
    :param request:
    :param company_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    weibo_instance = mongo_data.get_source_media_instance_dict(settings.MONGO_PARA)["weibo"]
    weibo_obj = weibo_instance.get_sort_news_objects(data_source_id_list)["today_sort_news_objects"].clone().limit(10)
    # 对weibo_obj进行序列化
    weibo_obj_list = common.serialize_news_obj(weibo_obj)
    contents = {"weibo_obj": weibo_obj_list}
    return JsonResponse(contents)


def baidu_zhidao(request, company_id):
    """
    百度知道
    :param request:
    :param company_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    baidu_zhidao_instance = mongo_data.get_source_media_instance_dict(paras=settings.MONGO_PARA)["baidu_zhidao"]
    baidu_zhidao_obj = baidu_zhidao_instance.get_sort_news_objects(
        data_source_id_list)["today_sort_news_objects"].clone().limit(10)
    # 对baidu_zhidao_obj进行序列化
    baidu_zhidao_obj_list = common.serialize_news_obj(baidu_zhidao_obj)
    contents = {"baidu_zhidao_obj": baidu_zhidao_obj_list}
    return JsonResponse(contents)


def app_info(request, company_id):
    """
    APP应用信息
    :param request:
    :param company_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    app_store_instance = source_media.AppStore(paras=settings.MONGO_PARA)
    app_bangdan_info = app_store_instance.get_app_bangdan_info_obj(data_source_id_list)
    app_comments_info = app_store_instance.get_app_comments_info(data_source_id_list)
    app_detail = app_store_instance.get_app_detail_obj(data_source_id_list)
    contents = {"app_bangdan_info": app_bangdan_info,
                "app_comments_info": app_comments_info,
                "app_detail": app_detail}

    return JsonResponse(contents)
