# -*- coding:utf-8 -*-
# import logging
from common import source_media
from common import mysql_data, settings
from django.http import JsonResponse
# Create your views here.


# logger = logging.getLogger(__name__)
# logger.info(__name__)
# logger.error(__name__)


def app_bd_curve(request):
    pass


def app_bd_info(request, app_id):
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(app_id))
    app_obj = source_media.AppStore(paras=settings.MONGO_PARA)
    app_bd_info_obj = app_obj.get_app_bd_info_obj(data_sour_id_list)
    return JsonResponse(app_bd_info_obj)


def app_comt(request, app_id):
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(app_id))
    app_obj = source_media.AppStore(paras=settings.MONGO_PARA)
    app_comt_info = app_obj.get_app_comts_info(data_sour_id_list)
    return JsonResponse(app_comt_info)
