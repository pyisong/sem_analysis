# -*- coding:utf-8 -*-
import source_media
import common
from collections import Counter
from settings import MONGO_PARA


def get_sour_med_ins_dict(paras):
    """
    得到所有数据源类的实例化对象
    :param paras:
    :return:
    :return:
    """
    sour_med_ins_dict = {
        "baidu_search": source_media.BaiDuSearch(paras),
        "baidu_tieba": source_media.BaiDuTieBa(paras),
        "baidu_zhidao": source_media.BaiDuZhiDao(paras),
        "weibo": source_media.WeiBo(paras),
        "weixin": source_media.WeiXin(paras),
        "zhihu": source_media.ZhiHu(paras)
        }

    return sour_med_ins_dict


def get_tal_infl(data_sour_id_list, paras, start_time=None, end_time=None):
    """
    存储最近7天的、上个7天的、今天的、昨天的和全部的不同情感值的 ，不同数据源的总的影响力
    :param end_time:
    :param start_time:
    :param paras:
    :return:
    :param data_sour_id_list:
    :return:
    """
    sour_med_ins_dict = get_sour_med_ins_dict(paras)
    tal_infl_dict = {}

    tal_usr_def_infl = 0
    tal_usr_def_neg_infl = 0
    tal_sev_infl = 0
    tal_last_sev_infl = 0
    tal_today_infl = 0
    tal_yest_infl = 0
    tal_today_neg_infl = 0
    tal_yest_neg_infl = 0
    # tal_sev_neg_infl = 0

    for value in sour_med_ins_dict.values():
        infl_dict = value.get_infl(data_sour_id_list, start_time=start_time, end_time=end_time)
        sent_infl_dict = value.get_sent_infl(data_sour_id_list, start_time=start_time, end_time=end_time)

        if start_time and end_time:
            tal_usr_def_infl += infl_dict.get("usr_def_infl") if infl_dict.get("usr_def_infl") else 0

            tal_usr_def_sent_infl_dict = sent_infl_dict.get("usr_def_sent_infl_dict")

            if tal_usr_def_sent_infl_dict:
                tal_usr_def_neg_infl += tal_usr_def_sent_infl_dict.get("negative")
            else:
                tal_usr_def_neg_infl += 0
        else:
            tal_sev_infl += infl_dict.get("sev_infl") if infl_dict.get("sev_infl") else 0
            tal_last_sev_infl += infl_dict.get("last_sev_infl") if infl_dict.get("last_sev_infl") else 0
            tal_today_infl += infl_dict.get("today_infl") if infl_dict.get("today_infl") else 0
            tal_yest_infl += infl_dict.get("yest_infl") if infl_dict.get("yest_infl") else 0

            tal_today_neg_infl += sent_infl_dict["today_sent_infl_dict"]["negative"]
            tal_yest_neg_infl += sent_infl_dict["yest_sent_infl_dict"]["negative"]
            # tal_sev_neg_infl += sent_infl_dict["sev_sent_infl_dict"]["negative"]

    if start_time and end_time:
        tal_infl_dict['tal_usr_def_neg_infl'] = tal_usr_def_neg_infl
        tal_infl_dict['tal_usr_def_infl'] = tal_usr_def_infl
    else:
        tal_infl_dict['tal_sev_infl'] = tal_sev_infl
        tal_infl_dict['tal_last_sev_infl'] = tal_last_sev_infl
        tal_infl_dict['tal_today_infl'] = tal_today_infl
        tal_infl_dict['tal_yest_infl'] = tal_yest_infl
        tal_infl_dict['tal_today_neg_infl'] = tal_today_neg_infl
        tal_infl_dict['tal_yest_neg_infl'] = tal_yest_neg_infl
        # tal_infl_dict['tal_sev_neg_infl'] = tal_sev_neg_infl
    return tal_infl_dict


def get_sent_infl(data_sour_id_list, paras):
    """
    包含所有数据源7天的不同情感值影响力的总值和每个数据源的情感值影响力
    :param paras:
    :return:
    :param data_sour_id_list:
    :return:
    """
    sour_med_ins_dict = get_sour_med_ins_dict(paras)
    tal_sev_sent_infl_dict = {
                                "tal_sev_neg_infl": 0,
                                "tal_sev_pos_infl": 0,
                                "tal_sev_neu_infl": 0,
                            }
    
    sev_sent_infl_dict = {}
    for key in sour_med_ins_dict:
        sev_sent_infl = sour_med_ins_dict[key].get_sent_infl(
            data_sour_id_list)['sev_sent_infl_dict']
        tal_sev_sent_infl_dict["tal_sev_neg_infl"] += sev_sent_infl["negative"]
        tal_sev_sent_infl_dict["tal_sev_pos_infl"] += sev_sent_infl["positive"]
        tal_sev_sent_infl_dict["tal_sev_neu_infl"] += sev_sent_infl["neutral"]
        sev_sent_infl_dict[key] = sev_sent_infl

    sent_infl_dict = {
        "tal_sev_sent_infl_dict": tal_sev_sent_infl_dict,
        "sev_sent_infl_dict": sev_sent_infl_dict
    }
    return sent_infl_dict


def get_tal_infl_chg(data_sour_id_list, paras, start_time=None, end_time=None):
    """
    得到不同时间段的总的影响力的变化值
    :param end_time:
    :param start_time:
    :param paras:
    :param data_sour_id_list:
    :return:
    """
    tal_infl_chg_dict = {}
    tal_infl_dict = get_tal_infl(data_sour_id_list, paras, start_time, end_time)

    if tal_infl_dict["tal_last_sev_infl"] > 0:
        tal_sev_infl_chg = (float(tal_infl_dict["tal_sev_infl"]) - float(tal_infl_dict["tal_last_sev_infl"])
                            ) / float(tal_infl_dict["tal_last_sev_infl"])
        
        tal_sev_infl_chg = "%.2f" % (tal_sev_infl_chg * 100) + "%"
    else:
        tal_sev_infl_chg = 0

    if tal_infl_dict["tal_yest_infl"] > 0:
        tal_day_infl_chg = (float(tal_infl_dict["tal_today_infl"]) - float(tal_infl_dict["tal_yest_infl"])
                            ) / float(tal_infl_dict["tal_yest_infl"])
        
        tal_day_infl_chg = "%.2f" % (tal_day_infl_chg * 100) + "%"
    else:
        tal_day_infl_chg = 0

    if tal_infl_dict["tal_yest_neg_infl"] > 0:
        tal_day_neg_infl_chg = (float(tal_infl_dict["tal_today_neg_infl"]) - float(tal_infl_dict["tal_yest_neg_infl"])
                                ) / float(tal_infl_dict["tal_yest_neg_infl"])
        
        tal_day_neg_infl_chg = "%.2f" % (tal_day_neg_infl_chg * 100) + "%"
    else:
        tal_day_neg_infl_chg = 0

    tal_infl_chg_dict["tal_sev_infl_chg"] = tal_sev_infl_chg
    tal_infl_chg_dict["tal_day_infl_chg"] = tal_day_infl_chg
    tal_infl_chg_dict["tal_day_neg_infl_chg"] = tal_day_neg_infl_chg

    contents = tal_infl_dict.copy()
    contents.update(tal_infl_chg_dict)
    return contents


def get_weibo_usr_loc_stas(data_sour_id_list, paras):
    """
    相关微博评论用户的所在地统计
    :param paras:
    :param data_sour_id_list:
    :return:
    """
    weibo_ins = source_media.WeiBo(paras)
    weibo_comt_loc_objs = weibo_ins.get_weibo_comt_loc(data_sour_id_list).clone()
    loc_list = []
    for item in weibo_comt_loc_objs:
        country = item.get("country") if item.get("country") else u"无"
        zone = item.get("zone") if item.get("zone") else u"无"
        # city = item.get("city") if item.get("city") else u"无"
        loc_list.append(country + "-" + zone)
    loc_stas_dict = dict(Counter(loc_list))
    return loc_stas_dict


def get_hot_med_sort_list(data_sour_id_list, paras):
    """
    得到按照新闻量排序的由媒体和新闻量组成的元组的列表
    :param data_sour_id_list:
    :param paras:
    :return:
    """
    sour_med_ins_dict = get_sour_med_ins_dict(paras)
    hot_med_list = []
    time_dict = common.get_time()
    for key in sour_med_ins_dict:
        hot_med_objs = sour_med_ins_dict[key].get_hot_med_obj(data_sour_id_list=data_sour_id_list,
                                                              start_time=time_dict["sev_ago_time"],
                                                              end_time=time_dict["now_time"])
        if key in ["baidu_search", "zhihu"]:
            for item in hot_med_objs:
                med = item.get("med") if item.get("author") else u"无"
                hot_med_list.append(med)
        if key in ["baidu_tieba", "weibo", "weixin"]:
            for item in hot_med_objs:
                author = item.get("author") if item.get("author") else u"无"
                hot_med_list.append(author)
    hot_med_stas_dict = dict(Counter(hot_med_list))
    hot_med_stas_list = []
    for k, v in hot_med_stas_dict.items():
        hot_med_stas_list.append((k, v))
    hot_med_stas_list.sort(key=lambda i: i[1], reverse=True)
    return hot_med_stas_list


def get_sort_news_objs_list(data_sour_id_list, paras, start_time, end_time):
    """
    获取默认时间内(7天)，不同数据源的新闻量按时间排序得到的对象列表
    :param end_time:
    :param start_time:
    :param paras:
    :param data_sour_id_list:
    :return:
    """
    sour_med_ins_dict = get_sour_med_ins_dict(paras)
    news_objs_list = []
    for key in sour_med_ins_dict:
        news_objs = sour_med_ins_dict[key].get_news_objs(data_sour_id_list=data_sour_id_list,
                                                         start_time=start_time,
                                                         end_time=end_time)
        news_objs_list.append(news_objs)
    sort_dif_news_objs_list = common.sort_dif_data_sour_obj(news_objs_list)
    return sort_dif_news_objs_list


def get_contents_expression(contents):
    """
    提取微信文章和评论中的表情
    :param contents:
    :return:
    """
    print contents
    pass

if __name__ == '__main__':
    print get_hot_med_sort_list(data_sour_id_list=[2], paras=MONGO_PARA)
