# -*- coding:utf-8 -*-
# from django.shortcuts import render
# import logging
from django.http import JsonResponse
from common import common, mysql_data, mongo_data, settings
# Create your views here.

# logger = logging.getLogger(__name__)
# logger.info(__name__)
# logger.error(__name__)


def company_search_exponent(request):
    """
    搜索曲线
    :param request:
    :return:
    """
    pass


def company_official_influence(request, company_id):
    """
    与企业相关的包含官网、微信官网、微博官网的新闻数量, 平均阅读量、点击量、转发量
    :param request:
    :param company_id:
    :return:
    """
    start_time = request.GET.get("start_time", common.default_start_time)
    end_time = request.GET.get("end_time", common.default_end_time)

    # 所有企业相关的data_source_id
    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    source_media_list = ["baidu_search", "weibo", "weixin"]
    source_media_instance_dict = mongo_data.get_source_media_instance_dict(paras=settings.MONGO_PARA)
    news_count_dict = {}
    avg_click_repost_read_dict = {}
    for source_media in source_media_list:
        news_count_dict[source_media] = source_media_instance_dict[source_media].get_news_count(
                                                                                                data_source_id_list,
                                                                                                start_time=start_time,
                                                                                                end_time=end_time)
        avg_click_repost_read_dict[source_media] =\
            source_media_instance_dict[source_media].get_avg_click_repost_read(data_source_id_list,
                                                                               start_time=start_time,
                                                                               end_time=end_time)
    contents = {
        "news_count_dict": news_count_dict,
        "avg_click_repost_read_dict": avg_click_repost_read_dict
    }
    return JsonResponse(contents)


def company_information_influence(request, company_id):
    """
    企业相关资讯影响力
    :param request:
    :param company_id:
    :return:
    """
    start_time = request.GET.get("start_time", common.default_start_time)
    end_time = request.GET.get("end_time", common.default_end_time)

    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    total_influence_dict = mongo_data.get_total_influence(data_source_id_list,
                                                          paras=settings.MONGO_PARA,
                                                          start_time=start_time,
                                                          end_time=end_time)

    total_user_defined_influence = total_influence_dict["total_user_defined_influence"]
    total_user_defined_sentiment_influence = total_influence_dict["total_user_defined_sentiment_influence"]

    contents = {"total_user_defined_influence": total_user_defined_influence,
                "total_user_defined_sentiment_influence": total_user_defined_sentiment_influence}

    return JsonResponse(contents)


def company_data_statistics(request, company_id):
    """
    企业相关各个媒体的影响力统计
    :param request:
    :param company_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    source_media_instance_dict = mongo_data.get_source_media_instance_dict(paras=settings.MONGO_PARA)
    single_media_dict = {}
    for key in source_media_instance_dict:
        single_media_dict[key] = source_media_instance_dict[key].get_influence(data_source_id_list)["seven_influence"]

    return JsonResponse(single_media_dict)


def company_weibo_user_location(request, company_id):
    """
    企业相关微博用户的地区分布详情
    :param request:
    :param company_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    location_statistics_dict = mongo_data.get_weibo_user_location_statistics(data_source_id_list,
                                                                             paras=settings.MONGO_PARA)
    return JsonResponse(location_statistics_dict)


def company_hot_media(request, company_id):
    """
    热门媒体排序
    :param request:
    :param company_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(company_id))
    hot_media_sort_list = mongo_data.get_hot_media_sort_list(data_source_id_list,
                                                             paras=settings.MONGO_PARA)[:10]
    contents = {"hot_media_sort_list": hot_media_sort_list}
    return JsonResponse(contents)
