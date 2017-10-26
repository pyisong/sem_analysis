# -*- coding:utf-8 -*-
# import logging
from common import source_media, common, mysql_data, settings
from django.http import JsonResponse
# Create your views here.


# logger = logging.getLogger(__name__)
# logger.info(__name__)
# logger.error(__name__)


def app_bd_curve(request):
    pass


def app_bd_info(request):
    """
    显示本应用最后一次出现在任意榜单的时间
    目标app榜单信息，以及目标app在榜单的前后app名称
    :param request:
    :return:
    """
    app_id = request.POST.get("app_id", 2)
    start_time = request.POST.get("start_time", common.default_start_time)
    end_time = request.POST.get("end_time", common.default_end_time)
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(app_id))
    app_obj = source_media.AppStore(paras=settings.MONGO_PARA)
    app_bd_info_obj = app_obj.get_app_bd_info_obj(data_sour_id_list=data_sour_id_list,
                                                  start_time=start_time, end_time=end_time)
    return JsonResponse(app_bd_info_obj)


def app_comt(request):
    """
    目标app的评论信息，星级评分统计、不同情感值统计
    :param request:
    :return:
    """
    app_id = request.POST.get("app_id", 2)
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(app_id))
    app_obj = source_media.AppStore(paras=settings.MONGO_PARA)
    app_comt_info = app_obj.get_app_comts_info(data_sour_id_list=data_sour_id_list)
    return JsonResponse(app_comt_info)
