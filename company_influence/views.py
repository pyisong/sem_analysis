# -*- coding:utf-8 -*-
# from django.shortcuts import render
# import logging
from django.http import JsonResponse
from common import common, mysql_data, mongo_data, settings
# Create your views here.

# logger = logging.getLogger(__name__)
# logger.info(__name__)
# logger.error(__name__)


def comp_search_exponent(request):
    """
    搜索曲线
    :param request:
    :return:
    """
    pass


def comp_offi_infl(request):
    """
    与企业相关的包含官网、微信官网、微博官网的新闻数量, 平均阅读量、点击量、转发量
    :param request:
    :return:
    """
    comp_id = request.POST.get("comp_id", 2)
    start_time = request.POST.get("start_time", common.default_start_time)
    end_time = request.POST.get("end_time", common.default_end_time)

    # 所有企业相关的data_sour_id
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(comp_id))
    sour_med_list = ["baidu_search", "weibo", "weixin"]
    sour_med_ins_dict = mongo_data.get_sour_med_ins_dict(paras=settings.MONGO_PARA)
    avg_cli_rep_comt_dict = {}
    for sour_med in sour_med_list:

        avg_cli_rep_comt_dict[sour_med] = sour_med_ins_dict[sour_med].get_avg_cli_rep_comt_dict(data_sour_id_list,
                                                                                                start_time=start_time,
                                                                                                end_time=end_time)

    return JsonResponse(avg_cli_rep_comt_dict)


def comp_inform_infl(request):
    """
    企业相关资讯影响力
    :param request:
    :return:
    """
    comp_id = request.POST.get("comp_id", 2)
    start_time = request.GET.get("start_time", common.default_start_time)
    end_time = request.GET.get("end_time", common.default_end_time)

    data_sour_id_list = mysql_data.get_data_sour_id_list(int(comp_id))
    tal_infl_dict = mongo_data.get_tal_infl(data_sour_id_list,
                                            paras=settings.MONGO_PARA,
                                            start_time=start_time,
                                            end_time=end_time)

    tal_usr_def_infl = tal_infl_dict["tal_usr_def_infl"]
    tal_usr_def_neg_infl = tal_infl_dict["tal_usr_def_neg_infl"]

    contents = {
        "tal_usr_def_infl": tal_usr_def_infl,
        "tal_usr_def_neg_infl": tal_usr_def_neg_infl
    }

    return JsonResponse(contents)


def comp_data_stas(request):
    """
    企业相关各个媒体的影响力统计
    :param request:
    :return:
    """
    comp_id = request.POST.get("comp_id", 2)
    start_time = request.GET.get("start_time", common.default_start_time)
    end_time = request.GET.get("end_time", common.default_end_time)
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(comp_id))
    sour_med_ins_dict = mongo_data.get_sour_med_ins_dict(paras=settings.MONGO_PARA)
    sgl_med_dict = {}
    for key in sour_med_ins_dict:
        sgl_med_dict[key] = sour_med_ins_dict[key].get_infl(data_sour_id_list=data_sour_id_list,
                                                            start_time=start_time,
                                                            end_time=end_time)["usr_def_infl"]

    return JsonResponse(sgl_med_dict)


def comp_weibo_usr_loc(request):
    """
    企业相关微博用户的地区分布详情
    :param request:
    :return:
    """
    comp_id = request.POST.get("comp_id", 2)
    start_time = request.GET.get("start_time", common.default_start_time)
    end_time = request.GET.get("end_time", common.default_end_time)
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(comp_id))
    loc_stas_dict = mongo_data.get_weibo_usr_loc_stas(data_sour_id_list,
                                                      paras=settings.MONGO_PARA,
                                                      start_time=start_time,
                                                      end_time=end_time)
    return JsonResponse(loc_stas_dict)


def comp_hot_med(request):
    """
    热门媒体排序
    :param request:
    :return:
    """
    comp_id = request.POST.get("comp_id", 2)
    start_time = request.GET.get("start_time", common.default_start_time)
    end_time = request.GET.get("end_time", common.default_end_time)
    data_sour_id_list = mysql_data.get_data_sour_id_list(int(comp_id))
    hot_med_sort_list = mongo_data.get_hot_med_sort_list(data_sour_id_list,
                                                         paras=settings.MONGO_PARA,
                                                         start_time=start_time,
                                                         end_time=end_time)[:10]
    contents = {"hot_med_sort_list": hot_med_sort_list}
    return JsonResponse(contents)
