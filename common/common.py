# -*- coding:utf-8 -*-
import datetime
from bson import ObjectId
import pymongo.cursor

# default_start_time = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')
# default_end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
default_start_time = "2013-01-01 00:00:00"
default_end_time = "2017-09-09 00:00:00"


def get_time():
    """
    得到不同时间段的时间
    :return:
    """
    time_dict = {}

    fourteen_ago_time = (datetime.datetime.now() - datetime.timedelta(days=14)).strftime('%Y-%m-%d %H:%M:%S')
    seven_ago_time = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')
    yesterday_time = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
    today_start_time = datetime.datetime.now().strftime('%Y-%m-%d 00:00:00')
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # time_dict['fourteen_ago_time'] = fourteen_ago_time
    # time_dict['seven_ago_time'] = seven_ago_time
    # time_dict['yesterday_time'] = yesterday_time
    # time_dict['today_start_time'] = today_start_time
    # time_dict['now_time'] = now_time

    time_dict['fourteen_ago_time'] = "2017-01-01 00:00:00"
    time_dict['seven_ago_time'] = "2013-01-01 00:00:00"
    time_dict['yesterday_time'] = "2017-01-01 00:00:00"
    time_dict['today_start_time'] = "2013-01-01 00:00:00"
    time_dict['now_time'] = "2017-09-09 00:00:00"
    return time_dict


def sort_dif_data_source_obj(args):
    """
    针对不同集合得到数据进行整合，以publish_time倒序排列
    :param args: 是不同数据源的对象
    :return:
    """
    news_list = []
    for obj in args:
        for news in obj:
            news.update({'_id': str(ObjectId(news.get("_id")))})
            news_list.append(news)
    news_list.sort(key=lambda i: i["publish_time"], reverse=True)
    return news_list


def serialize_news_obj(news_obj):
    """
    序列化查找对象
    :param news_obj:
    :return:
    """
    news_obj_list = []
    if isinstance(news_obj, pymongo.cursor.Cursor):
        for item in news_obj:
            if item.get("_id"):
                item.update({'_id': str(ObjectId(item.get("_id")))})
            news_obj_list.append(item)
        return news_obj_list
    else:
        if news_obj.get("_id"):
            news_obj.update({'_id': str(ObjectId(news_obj.get("_id")))})
        return news_obj


def get_haosou_exponent():
    """
    获得好搜的搜索指数
    :return:
    """
    pass
