# -*- coding:utf-8 -*-
# import logging
from django.http import JsonResponse
from common import mysql_data, mongo_data, settings, common
# Create your views here.

# logger = logging.getLogger(__name__)
# logger.info(__name__)
# logger.error(__name__)


def product_search_exponent(request):
    """
    搜索曲线
    :param request:
    :return:
    """
    pass


def product_sentiment_statistics(request, product_id):
    """
    统计7天，产品相关微信及相关微信评论中的表情的前三名
    :param request:
    :param product_id:
    :return:
    """
    pass


def product_information_influence(request, product_id):
    """
    产品相关资讯影响力
    :param request:
    :param product_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(product_id))
    total_influence_dict = mongo_data.get_total_influence(data_source_id_list, paras=settings.MONGO_PARA)
    total_seven_influence = total_influence_dict["total_seven_influence"]
    total_seven_negative_influence = total_influence_dict["total_seven_negative_influence"]

    contents = {
        "total_seven_influence": total_seven_influence,
        "total_seven_negative_influence": total_seven_negative_influence
    }

    return JsonResponse(contents)


def product_data_statistics(request, product_id):
    """
    产品相关各个媒体的影响力统计
    :param request:
    :param product_id:
    :return:
    """
    start_time = request.POST.get("start_time", common.default_start_time)
    end_time = request.POST.get("end_time", common.default_end_time)
    data_source_id_list = mysql_data.get_data_source_id_list(int(product_id))
    source_media_instance_dict = mongo_data.get_source_media_instance_dict(paras=settings.MONGO_PARA)
    single_media_dict = {}
    for key in source_media_instance_dict:
        single_media_dict[key] =\
            source_media_instance_dict[key].get_influence(data_source_id_list,
                                                          start_time=start_time,
                                                          end_time=end_time)["user_defined_influence"]

    return JsonResponse(single_media_dict)


def product_weibo_user_location(request, product_id):
    """
    产品相关微博用户的地区分布详情
    :param request:
    :param product_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(product_id))
    location_statistics_dict = mongo_data.get_weibo_user_location_statistics(data_source_id_list,
                                                                             paras=settings.MONGO_PARA)
    return JsonResponse(location_statistics_dict)


def product_hot_media(request, product_id):
    """
    产品相关热门媒体排序
    :param request:
    :param product_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(product_id))
    hot_media_sort_list = mongo_data.get_hot_media_sort_list(data_source_id_list,
                                                             paras=settings.MONGO_PARA)[:10]
    contents = {"hot_media_sort_list": hot_media_sort_list}
    return JsonResponse(contents)
