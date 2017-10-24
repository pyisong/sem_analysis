# -*- coding:utf-8 -*-
# import logging
from django.http import JsonResponse
from common import mongo_data, mysql_data, settings, common
# Create your views here.

# logger = logging.getLogger(__name__)
# logger.info(__name__)
# logger.error(__name__)


def event_infl_overview(request, event_id):
    """
    事件相关的各个数据源的情感值影响力的比例值
    :param request:
    :param event_id:
    :return:
    """
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(event_id))
    sour_med_ins_dict = mongo_data.get_sour_med_ins_dict(paras=settings.MONGO_PARA)
    contents = {}
    for key in sour_med_ins_dict:
        contents[key] = sour_med_ins_dict[key].get_sent_infl(data_sour_id_list)["seven_sent_infl_dict"]
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

    data_sour_id_list = mysql_data.get_data_sour_id_list(int(event_id))
    sort_dif_news_objs = mongo_data.get_sort_news_objs_list(data_sour_id_list,
                                                            paras=settings.MONGO_PARA,
                                                            start_time=start_time,
                                                            end_time=end_time)
    contents = {"sort_dif_news_objs": sort_dif_news_objs}
    return JsonResponse(contents)


def event_atti_stas(request, event_id):
    """
    媒体或用户对事件的态度统计
    :param request:
    :param event_id:
    :return:
    """
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(event_id))
    sour_med_ins_dict = mongo_data.get_sour_med_ins_dict(paras=settings.MONGO_PARA)
    atti_type = request.POST.get("atti_type")
    sent_dict = {"negative": 0, "positive": 0, "neutral": 0}

    if atti_type == "media":
        for ins in [sour_med_ins_dict["baidu_search"], sour_med_ins_dict["weixin"]]:
            objs = ins.get_sent_stas(data_sour_id_list=data_sour_id_list, start_time=None, end_time=None)
            for obj in objs:
                sent_dict[obj["_id"]] += obj["count"]

    if atti_type == "user":
        for ins in [
            sour_med_ins_dict["baidu_tieba"],
            sour_med_ins_dict["baidu_zhidao"],
            sour_med_ins_dict["weibo"],
            sour_med_ins_dict["zhihu"]
        ]:
            objs = ins.get_sent_stas(data_sour_id_list=data_sour_id_list, start_time=None, end_time=None)
            for obj in objs:
                sent_dict[obj["_id"]] += obj["count"]

    return JsonResponse(sent_dict)
