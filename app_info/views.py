# -*- coding:utf-8 -*-
# import logging
from common import source_media
from common import mysql_data, settings
from django.http import JsonResponse
# Create your views here.


# logger = logging.getLogger(__name__)
# logger.info(__name__)
# logger.error(__name__)


def app_bangdan_curve(request):
    pass


def app_bangdan_info(request, app_id):
    data_source_id_list = mysql_data.get_data_source_id_list(int(app_id))
    app_obj = source_media.AppStore(paras=settings.MONGO_PARA)
    app_bangdan_info_obj = app_obj.get_app_bangdan_info_obj(data_source_id_list)
    return JsonResponse(app_bangdan_info_obj)


def app_comment(request, app_id):
    data_source_id_list = mysql_data.get_data_source_id_list(int(app_id))
    app_obj = source_media.AppStore(paras=settings.MONGO_PARA)
    app_comment_info = app_obj.get_app_comments_info(data_source_id_list)
    return JsonResponse(app_comment_info)
