# -*- coding:utf-8 -*-
import pymongo
import common
import pymysql
import logging
from collections import Counter


MONGO_PARA = "mongodb://access_mongo:donewsusemongodbby20170222@slave07:27017/admin?readPreference=secondaryPreferred"

def get_mysql_db():
    mysql_db = None
    if mysql_db is None:
        mysql_db = pymysql.Connection(host="59.110.52.178",
                                      user="admin001",
                                      password="donews1234",
                                      database="sem_db",
                                      charset="utf8")
    return mysql_db


def get_mongodb_client(paras):
    try:
        client = pymongo.MongoClient(paras)
        return client
    except Exception as e:
        logging.error("Connect mongo Error:", e)
        return None


if __name__ == "__main__":
    client = get_mongodb_client(MONGO_PARA)
    db = client["sem"]
    obj = db["search_weibo"].find({"data_source_id": 2}).sort("-publish_time")
    obj1 = db["search_weibo"].find({"data_source_id": 2,
                                   "publish_time": {"$gte": "2017-01-03 19:00:00",
                                                    "$lte": "2017-01-03 19:20:00"}})
    obj2 = db["zhidao"].find({"data_source_id": "t_20170301_005",
                              "publish_time": {"$gte": "2016-05-06 00:00:00",
                                               "$lte": "2017-01-03 19:20:00"}})

    # db["search_weibo"].update({"weibo_id": "1649173367"}, {'$set': {'click_count': 0}})
    # {'id': {'$gt': 0}}, {'$set': {'click_count': 0}}
    # o = db["search_weibo"].find({"weibo_id": "1649173367"})
    # print o.count()
    # print o[0]["click_count"]
    # # 2017-01-03 19:14:00
    # # 2017-01-03 19:03:00
    # print obj1.count()
    # print obj2.count()
    # obj_list = []
    # for item1 in obj1:
    #     obj_list.append(item1)
    # for item2 in obj2:
    #     obj_list.append(item2)
    #
    # # for item in obj1:
    # #     print item['publish_time'],  item["data_source_id"]
    # print len(obj_list)
    # print obj_list
    # for i in obj_list:
    #     print i["publish_time"]
    # obj_list.sort(key=lambda item: item["publish_time"], reverse=True)
    # print "*" * 20
    # for i in obj_list:
    #     print i["publish_time"]
    #
    # print "*" * 20
    # ls = [obj1, obj2]
    # news_list = common.sort_dif_data_source_obj(ls)
    # for i in news_list:
    #     print i["publish_time"], i["_id"]
    #
    # print "*" * 20
    # db = get_mysql_db()
    # sql = 'SELECT * FROM monitor_app_info limit 1'
    # cursor = db.cursor()
    # cursor.execute(sql)
    # print cursor.fetchall()
    # print "=" * 30
    # obj1 = db["search_weibo"].find({"$or": [{"data_source_id": i} for i in [2, "t_20170301_007"]],
    #                                }).count()
    # print obj1
    # print type(db["search_weibo"])
    result = db["search_weibo"].aggregate([{"$group": {"_id": "$data_source_id", "count": {"$sum": 1}}}])
    print result
    temp_dict = {}
    for i in result:
        print i
        temp_dict[i['_id']] = i["count"]
    print temp_dict
    print type(result)

    # print "=" * 30
    # weibo_comment_location_objects = db["search_weibo_comment"].find({"data_source_id": 2},
    #                                                                  {"_id": 0, "country": 1, "zone": 1, "city": 1})
    # # print weibo_comment_location_objects[0]
    # location_list = []
    # for i in weibo_comment_location_objects:
    #     country = i.get("country") if i.get("country") else " "
    #     zone = i.get("zone") if i.get("zone") else u"无"
    #     city = i.get("city") if i.get("city") else u"无"
        # if country:
        #     country = i.get("country")
        # else:
        #     country = " "
        #
        # if zone:
        #     zone = i.get("zone")
        # else:
        #     zone = " "
        #
        # if city:
        #     city = i.get("city")
        # else:
        #     city = " "
        # print country
        # print zone
        # print city
    #     location_list.append(country + "-" + zone)
    # # print location_list
    # # for j in location_list:
    # #     print j
    #
    # dic = Counter(location_list)
    # dic = dict(dic)
    # temp_list = []
    # for k, v in dic.items():
    #     temp_list.append((k, v))
    # temp_list.sort(key=lambda temp: temp[1], reverse=True)
    # print temp_list[:2]
    # print dic[u"中国-北京"]
    # for item in dic.items():
    #     print item[0], item[1]
