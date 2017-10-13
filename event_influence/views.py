# -*- coding:utf-8 -*-
# import logging
from django.http import JsonResponse
from common import mongo_data, mysql_data, settings, common
# Create your views here.

# logger = logging.getLogger(__name__)
# logger.info(__name__)
# logger.error(__name__)


def event_influence_overview(request, event_id):
    """
    事件相关的各个数据源的情感值影响力的比例值
    :param request:
    :param event_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(event_id))
    source_media_instance_dict = mongo_data.get_source_media_instance_dict(paras=settings.MONGO_PARA)
    contents = {}
    for key in source_media_instance_dict:
        contents[key] = \
            source_media_instance_dict[key].get_sentiment_influence(
                data_source_id_list)["seven_sentiment_influence_dict"]
    return JsonResponse(contents)


def event_hot_word(request):
    """
    事件相关热词(前20个)
    :param request:
    :return:
    """
    pass


def event_propagation_trace(request, event_id):
    """
    事件传播轨迹
    :param request:
    :param event_id:
    :return:
    """
    start_time = request.GET.get("start_time", common.default_start_time)
    end_time = request.GET.get("end_time", common.default_end_time)

    data_source_id_list = mysql_data.get_data_source_id_list(int(event_id))
    sort_dif_news_objects = mongo_data.get_sort_news_objects_list(data_source_id_list,
                                                                  paras=settings.MONGO_PARA,
                                                                  start_time=start_time,
                                                                  end_time=end_time)
    contents = {"sort_dif_news_objects": sort_dif_news_objects}
    return JsonResponse(contents)


def event_attitude_statistics(request, event_id):
    """
    媒体或用户对事件的态度统计
    :param request:
    :param event_id:
    :return:
    """
    data_source_id_list = mysql_data.get_data_source_id_list(int(event_id))
    source_media_instance_dict = mongo_data.get_source_media_instance_dict(paras=settings.MONGO_PARA)
    attitude_type = request.POST.get("attitude_type")
    sentiment_dict = {"negative": 0, "positive": 0, "neutral": 0}

    if attitude_type == "media":
        for instance in [source_media_instance_dict["baidu_search"], source_media_instance_dict["weixin"]]:
            objects = instance.get_sentiment_statistics_objects(data_source_id_list=data_source_id_list,
                                                                start_time=None,
                                                                end_time=None)
            for obj in objects:
                sentiment_dict[obj["_id"]] += obj["count"]

    if attitude_type == "user":
        for instance in [
            source_media_instance_dict["baidu_tieba"],
            source_media_instance_dict["baidu_zhidao"],
            source_media_instance_dict["weibo"],
            source_media_instance_dict["zhihu"]
        ]:
            objects = instance.get_sentiment_statistics_objects(data_source_id_list=data_source_id_list,
                                                                start_time=None,
                                                                end_time=None)
            for obj in objects:
                sentiment_dict[obj["_id"]] += obj["count"]

    return JsonResponse(sentiment_dict)
