# -*- coding:utf-8 -*-
# import logging
from django.http import JsonResponse
from common import mysql_data, mongo_data, settings, common
# Create your views here.

# logger = logging.getLogger(__name__)
# logger.info(__name__)
# logger.error(__name__)


def pro_search_exponent(request):
    """
    搜索曲线
    :param request:
    :return:
    """
    pass


def pro_weixin_expression(request, pro_id):
    """
    统计7天，产品相关微信及相关微信评论中的表情的前三名
    :param request:
    :param pro_id:
    :return:
    """
    pass


def pro_inform_infl(request, pro_id):
    """
    产品相关资讯影响力
    :param request:
    :param pro_id:
    :return:
    """
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(pro_id))
    tal_infl_dict = mongo_data.get_tal_infl(data_sour_id_list, paras=settings.MONGO_PARA)
    tal_sev_infl = tal_infl_dict["tal_sev_infl"]
    tal_sev_neg_infl = tal_infl_dict["tal_sev_neg_infl"]

    contents = {
        "tal_sev_infl": tal_sev_infl,
        "tal_sev_neg_infl": tal_sev_neg_infl
    }

    return JsonResponse(contents)


def pro_data_stas(request, pro_id):
    """
    产品相关各个媒体的影响力统计
    :param request:
    :param pro_id:
    :return:
    """
    start_time = request.POST.get("start_time", common.default_start_time)
    end_time = request.POST.get("end_time", common.default_end_time)
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(pro_id))
    sour_med_ins_dict = mongo_data.get_sour_med_ins_dict(paras=settings.MONGO_PARA)
    sgl_med_dict = {}
    for key in sour_med_ins_dict:
        sgl_med_dict[key] = sour_med_ins_dict[key].get_infl(data_sour_id_list,
                                                            start_time=start_time, end_time=end_time)["usr_def_infl"]

    return JsonResponse(sgl_med_dict)


def pro_weibo_usr_loc(request, pro_id):
    """
    产品相关微博用户的地区分布详情
    :param request:
    :param pro_id:
    :return:
    """
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(pro_id))
    loc_stas_dict = mongo_data.get_weibo_usr_loc_stas(data_sour_id_list, paras=settings.MONGO_PARA)
    return JsonResponse(loc_stas_dict)


def pro_hot_med(request, pro_id):
    """
    产品相关热门媒体排序
    :param request:
    :param pro_id:
    :return:
    """
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(pro_id))
    hot_med_sort_list = mongo_data.get_hot_med_sort_list(data_sour_id_list, paras=settings.MONGO_PARA)[:10]
    contents = {"hot_med_sort_list": hot_med_sort_list}
    return JsonResponse(contents)
