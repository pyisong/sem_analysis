# -*- coding:utf-8 -*-
import pymongo
import common
import pymysql
import logging
from collections import Counter


# MONGO_PARA = "mongodb://access_mongo:donewsusemongodbby20170222@slave07:27017/admin?readPreference=secondaryPreferred"
MONGO_PARA = "mongodb://localhost:27017"

DB = "sem_test"

INFL_SCALE = {
    "baidu_search": 0.3,
    "baidu_tieba": 0.6,
    "baidu_zhidao": 0.8,
    "weibo": 0.6,
    "weixin": 0.9,
    "zhihu": 0.3
}


def get_mysql_db():
    mysql_db = None
    if mysql_db is None:
        mysql_db = pymysql.Connection(host="59.110.52.178",
                                      user="admin001",
                                      password="donews1234",
                                      database="sem_db",
                                      charset="utf8")
    return mysql_db


def get_mysql_db_test():
    mysql_db = None
    if mysql_db is None:
        mysql_db = pymysql.Connection(host="localhost",
                                      user="root",
                                      password="mysql",
                                      database="sem_analysis",
                                      charset="utf8")
    return mysql_db


def get_mongodb_client(paras):
    try:
        cli = pymongo.MongoClient(paras)
        return cli
    except Exception as e:
        logging.error("Connect mongo Error:", e)
        return None


if __name__ == "__main__":
    client = get_mongodb_client(MONGO_PARA)
    print client.database_names()
    # db = client["sem_test"]
    # obj = db["search_weibo"].find({"data_sour_id": 2}).sort("-publish_time")
    # obj1 = db["search_weibo"].find({"data_sour_id": 2,
    #                                "publish_time": {"$gte": "2017-01-03 19:00:00",
    #                                                 "$lte": "2017-01-03 19:20:00"}})
    # obj2 = db["zhidao"].find({"data_sour_id": "t_20170301_005",
    #                           "publish_time": {"$gte": "2016-05-06 00:00:00",
    #                                            "$lte": "2017-01-03 19:20:00"}})

    # result = db["search_weibo"].aggregate([{"$group": {"_id": "$data_sour_id", "count": {"$sum": 1}}}])
    # print result
    # temp_dict = {}
    # for i in result:
    #     print i
    #     temp_dict[i['_id']] = i["count"]
    # print temp_dict
    # print type(result)

    # result = db["search_baidu"].aggregate([
    #                                  {"$match": {"$or": [{"data_sour_id": i} for i in [1, 2, 3]]}},
    #                                                               {"$group": {"_id": "$sentiment",
    #                                                                           "count": {"$sum": 1}}}])
    #
    # for i in result:
    #     print i
    #
    # count = db["search_baidu"].find({}).count()
    # print count
