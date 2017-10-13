# -*- coding:utf-8 -*-
import source_media
import common
from collections import Counter


def get_source_media_instance_dict(paras):
    """
    得到所有数据源类的实例化对象
    :param paras:
    :return:
    :return:
    """
    source_media_instance_dict = {"baidu_search": source_media.BaiDuSearch(paras),
                                  "baidu_tieba": source_media.BaiDuTieBa(paras),
                                  "baidu_zhidao": source_media.BaiDuZhiDao(paras),
                                  "weibo": source_media.WeiBo(paras),
                                  "weixin": source_media.WeiXin(paras),
                                  "zhihu": source_media.ZhiHu(paras)}
    return source_media_instance_dict


def get_total_influence(data_source_id_list, paras, start_time=None, end_time=None):
    """
    存储最近7天的、上个7天的、今天的、昨天的和全部的不同情感值的 ，不同数据源的总的影响力
    :param end_time:
    :param start_time:
    :param paras:
    :return:
    :param data_source_id_list:
    :return:
    """
    source_media_instance_dict = get_source_media_instance_dict(paras)
    total_influence_dict = {}

    total_seven_influence = 0
    total_last_seven_influence = 0
    total_today_influence = 0
    total_yesterday_influence = 0
    total_today_negative_influence = 0
    total_yesterday_negative_influence = 0
    total_seven_negative_influence = 0
    total_user_defined_sentiment_influence = 0
    total_user_defined_influence = 0

    for value in source_media_instance_dict.values():
        influence_dict = value.get_influence(data_source_id_list, start_time=start_time, end_time=end_time)
        sentiment_influence_dict = value.get_sentiment_influence(data_source_id_list,
                                                                 start_time=start_time,
                                                                 end_time=end_time)

        total_user_defined_influence +=\
            influence_dict.get("user_defined_influence") if influence_dict.get("user_defined_influence") else 0
        total_seven_influence +=\
            influence_dict.get("seven_influence") if influence_dict.get("seven_influence") else 0
        total_last_seven_influence +=\
            influence_dict.get("last_seven_influence") if influence_dict.get("last_seven_influence") else 0
        total_today_influence +=\
            influence_dict.get("today_influence") if influence_dict.get("today_influence") else 0
        total_yesterday_influence +=\
            influence_dict.get("yesterday_influence") if influence_dict.get("yesterday_influence") else 0

        total_user_defined_sentiment_influence_dict =\
            sentiment_influence_dict.get("user_defined_sentiment_influence_dict")

        if total_user_defined_sentiment_influence_dict:
            total_user_defined_sentiment_influence += total_user_defined_sentiment_influence_dict.get("negative")
        else:
            total_user_defined_sentiment_influence += 0

        total_today_negative_influence += \
            sentiment_influence_dict["today_sentiment_influence_dict"]["negative"]
        total_yesterday_negative_influence += \
            sentiment_influence_dict["yesterday_sentiment_influence_dict"]["negative"]
        total_seven_negative_influence += \
            sentiment_influence_dict["seven_sentiment_influence_dict"]["negative"]

    total_influence_dict['total_seven_influence'] = total_seven_influence
    total_influence_dict['total_last_seven_influence'] = total_last_seven_influence
    total_influence_dict['total_today_influence'] = total_today_influence
    total_influence_dict['total_yesterday_influence'] = total_yesterday_influence
    total_influence_dict['total_today_negative_influence'] = total_today_negative_influence
    total_influence_dict['total_yesterday_negative_influence'] = total_yesterday_negative_influence
    total_influence_dict['total_seven_negative_influence'] = total_seven_negative_influence
    total_influence_dict['total_user_defined_sentiment_influence'] = total_seven_negative_influence
    total_influence_dict['total_user_defined_influence'] = total_seven_negative_influence
    return total_influence_dict


def get_sentiment_influence(data_source_id_list, paras):
    """
    包含所有数据源7天的不同情感值影响力的总值和每个数据源的情感值影响力
    :param paras:
    :return:
    :param data_source_id_list:
    :return:
    """
    source_media_instance_dict = get_source_media_instance_dict(paras)
    total_seven_sentiment_influence_dict = {
                                            "total_seven_negative_influence": 0,
                                            "total_seven_positive_influence": 0,
                                            "total_seven_neutral_influence": 0
                                            }
    seven_sentiment_influence_dict = {}
    for key in source_media_instance_dict:
        seven_sentiment_influence = source_media_instance_dict[key].get_sentiment_influence(
            data_source_id_list)['seven_sentiment_influence_dict']
        total_seven_sentiment_influence_dict["total_seven_negative_influence"] += seven_sentiment_influence["negative"]
        total_seven_sentiment_influence_dict["total_seven_positive_influence"] += seven_sentiment_influence["positive"]
        total_seven_sentiment_influence_dict["total_seven_neutral_influence"] += seven_sentiment_influence["neutral"]
        seven_sentiment_influence_dict[key] = seven_sentiment_influence

    sentiment_influence_dict = {
        "total_seven_sentiment_influence_dict": total_seven_sentiment_influence_dict,
        "seven_sentiment_influence_dict": seven_sentiment_influence_dict
    }
    return sentiment_influence_dict


def get_total_influence_change(data_source_id_list, paras, start_time=None, end_time=None):
    """
    得到不同时间段的总的影响力的变化值
    :param end_time:
    :param start_time:
    :param paras:
    :param data_source_id_list:
    :return:
    """
    total_influence_change_dict = {}
    total_influence_dict = get_total_influence(data_source_id_list, paras, start_time, end_time)

    if total_influence_dict["total_last_seven_influence"] > 0:
        total_seven_influence_change = (float(total_influence_dict["total_seven_influence"]) -
                                        float(total_influence_dict["total_last_seven_influence"])
                                        ) / float(total_influence_dict["total_last_seven_influence"])
        total_seven_influence_change = "%.2f" % (total_seven_influence_change * 100) + "%"
    else:
        total_seven_influence_change = 0

    if total_influence_dict["total_yesterday_influence"] > 0:
        total_day_influence_change = (float(total_influence_dict["total_today_influence"]) -
                                      float(total_influence_dict["total_yesterday_influence"])
                                      ) / float(total_influence_dict["total_yesterday_influence"])
        total_day_influence_change = "%.2f" % (total_day_influence_change * 100) + "%"
    else:
        total_day_influence_change = 0

    if total_influence_dict["total_yesterday_negative_influence"] > 0:
        total_day_negative_influence_change = (float(total_influence_dict["total_today_negative_influence"]) -
                                               float(total_influence_dict["total_yesterday_negative_influence"])
                                               ) / float(total_influence_dict["total_yesterday_negative_influence"])
        total_day_negative_influence_change = "%.2f" % (total_day_negative_influence_change * 100) + "%"
    else:
        total_day_negative_influence_change = 0

    total_influence_change_dict["total_seven_influence_change"] = total_seven_influence_change
    total_influence_change_dict["total_day_influence_change"] = total_day_influence_change
    total_influence_change_dict["total_day_negative_influence_change"] = total_day_negative_influence_change
    return total_influence_change_dict


def get_weibo_user_location_statistics(data_source_id_list, paras):
    """
    相关微博评论用户的所在地统计
    :param paras:
    :param data_source_id_list:
    :return:
    """
    weibo_instance = source_media.WeiBo(paras)
    weibo_comment_location_objects = weibo_instance.get_weibo_comment_location(data_source_id_list).clone()
    location_list = []
    for item in weibo_comment_location_objects:
        country = item.get("country") if item.get("country") else u"无"
        zone = item.get("zone") if item.get("zone") else u"无"
        # city = item.get("city") if item.get("city") else u"无"
        location_list.append(country + "-" + zone)
    location_statistics_dict = dict(Counter(location_list))
    return location_statistics_dict


def get_hot_media_sort_list(data_source_id_list, paras):
    """
    得到按照新闻量排序的由媒体和新闻量组成的元组的列表
    :param data_source_id_list:
    :param paras:
    :return:
    """
    source_media_instance_dict = get_source_media_instance_dict(paras)
    hot_media_list = []
    for key in source_media_instance_dict:
        hot_media_objects = source_media_instance_dict[key].get_hot_media_objects(data_source_id_list)
        if key in ["baidu_search", "zhihu"]:
            for item in hot_media_objects:
                media = item.get("media") if item.get("author") else u"无"
                hot_media_list.append(media)
        if key in ["baidu_tieba", "weibo", "weixin"]:
            for item in hot_media_objects:
                author = item.get("author") if item.get("author") else u"无"
                hot_media_list.append(author)
    hot_media_statistics_dict = dict(Counter(hot_media_list))
    hot_media_statistics_list = []
    for k, v in hot_media_statistics_dict.items():
        hot_media_statistics_list.append((k, v))
    hot_media_statistics_list.sort(key=lambda i: i[1], reverse=True)
    return hot_media_statistics_list


def get_sort_news_objects_list(data_source_id_list, paras, start_time, end_time):
    """
    获取默认时间内(7天)，不同数据源的新闻量按时间排序得到的对象列表
    :param end_time:
    :param start_time:
    :param paras:
    :param data_source_id_list:
    :return:
    """
    source_media_instance_dict = get_source_media_instance_dict(paras)
    news_objects_list = []
    for key in source_media_instance_dict:
        news_objects = source_media_instance_dict[key].get_news_objects(data_source_id_list=data_source_id_list,
                                                                        start_time=start_time,
                                                                        end_time=end_time)
        news_objects_list.append(news_objects)
    sort_dif_news_objects_list = common.sort_dif_data_source_obj(news_objects_list)
    return sort_dif_news_objects_list


def get_contents_expression(contents):
    """
    提取微信文章和评论中的表情
    :param contents:
    :return:
    """
    print contents
    pass
