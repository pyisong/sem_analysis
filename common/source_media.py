# -*- coding:utf-8 -*-

from settings import get_mongodb_client
from common import get_time, serialize_news_obj


class BaseSourceMedia(object):

    def __init__(self, paras):
        """
        连接到指定的mongodb数据库
        """
        self._db = get_mongodb_client(paras)['sem_test']
        self.time_dict = get_time()

    def _get_news(self, data_source_id_list, start_time, end_time, sentiment=None):
        """
        新闻影响力和新闻对象
        :param data_source_id_list:
        :param start_time:
        :param end_time:
        :param sentiment:
        :return:
        """
        return {}

    def get_influence(self, data_source_id_list, start_time=None, end_time=None):
        """
        最近7天、上个7天、今天、昨天的影响力
        :param end_time:
        :param start_time:
        :param data_source_id_list:
        :return:
        """
        influence_dict = {}
        if start_time and end_time:
            user_defined_influence = self._get_news(data_source_id_list=data_source_id_list,
                                                    start_time=start_time,
                                                    end_time=end_time)['influence']
            influence_dict["user_defined_influence"] = user_defined_influence

        seven_influence = self._get_news(data_source_id_list=data_source_id_list,
                                         start_time=self.time_dict["seven_ago_time"],
                                         end_time=self.time_dict["now_time"])['influence']

        last_seven_influence = self._get_news(data_source_id_list=data_source_id_list,
                                              start_time=self.time_dict["fourteen_ago_time"],
                                              end_time=self.time_dict["seven_ago_time"])['influence']

        today_influence = self._get_news(data_source_id_list=data_source_id_list,
                                         start_time=self.time_dict["today_start_time"],
                                         end_time=self.time_dict["now_time"])['influence']

        yesterday_influence = self._get_news(data_source_id_list=data_source_id_list,
                                             start_time=self.time_dict["yesterday_time"],
                                             end_time=self.time_dict["today_start_time"])['influence']

        influence_dict["seven_influence"] = seven_influence
        influence_dict["last_seven_influence"] = last_seven_influence
        influence_dict["today_influence"] = today_influence
        influence_dict["yesterday_influence"] = yesterday_influence
        return influence_dict

    def get_sentiment_influence(self, data_source_id_list, start_time=None, end_time=None):
        """
        根据情感值分别得到不同情感值的影响力
        :param end_time:
        :param start_time:
        :param data_source_id_list:
        :return:
        """
        sentiment_influence_dict = {}  # 存储不同时间段、不同情感值的影响力
        today_sentiment_influence_dict = {}
        yesterday_sentiment_influence_dict = {}
        seven_sentiment_influence_dict = {}
        user_defined_sentiment_influence_dict = {}
        sentiment_list = ['negative', 'positive', 'neutral']

        for sentiment in sentiment_list:
            if start_time and end_time:
                user_defined_sentiment_influence = self._get_news(data_source_id_list=data_source_id_list,
                                                                  start_time=start_time,
                                                                  end_time=end_time,
                                                                  sentiment=sentiment)['influence']
                user_defined_sentiment_influence_dict[sentiment] = user_defined_sentiment_influence

            today_sentiment_influence = self._get_news(data_source_id_list=data_source_id_list,
                                                       start_time=self.time_dict["today_start_time"],
                                                       end_time=self.time_dict["now_time"],
                                                       sentiment=sentiment)['influence']
            yesterday_sentiment_influence = self._get_news(data_source_id_list=data_source_id_list,
                                                           start_time=self.time_dict["today_start_time"],
                                                           end_time=self.time_dict["now_time"],
                                                           sentiment=sentiment)['influence']
            seven_sentiment_influence = self._get_news(data_source_id_list=data_source_id_list,
                                                       start_time=self.time_dict["seven_ago_time"],
                                                       end_time=self.time_dict["now_time"],
                                                       sentiment=sentiment)['influence']

            today_sentiment_influence_dict[sentiment] = today_sentiment_influence
            yesterday_sentiment_influence_dict[sentiment] = yesterday_sentiment_influence
            seven_sentiment_influence_dict[sentiment] = seven_sentiment_influence

        sentiment_influence_dict["today_sentiment_influence_dict"] = today_sentiment_influence_dict
        sentiment_influence_dict["yesterday_sentiment_influence_dict"] = yesterday_sentiment_influence_dict
        sentiment_influence_dict["seven_sentiment_influence_dict"] = seven_sentiment_influence_dict
        sentiment_influence_dict["user_defined_sentiment_influence_dict"] = user_defined_sentiment_influence_dict
        return sentiment_influence_dict

    def get_week_influence_change(self, data_source_id_list):
        """
        本周与上周影响力的对比
        :param data_source_id_list:
        :return:
        """
        last_week_influence = self._get_news(data_source_id_list=data_source_id_list,
                                             start_time=self.time_dict["fourteen_ago_time"],
                                             end_time=self.time_dict["seven_ago_time"])['influence']
        current_week_influence = self._get_news(data_source_id_list=data_source_id_list,
                                                start_time=self.time_dict["seven_ago_time"],
                                                end_time=self.time_dict["now_time"])['influence']

        week_influence_change = (float(current_week_influence) - float(last_week_influence))/float(last_week_influence)
        week_influence_change = "%.2f" % (week_influence_change * 100) + "%"
        return week_influence_change

    def get_day_influence_change(self, data_source_id_list):
        """
        单个数据源的今天与昨天影响力对比
        :param data_source_id_list:
        :return:
        """
        yesterday_influence = self._get_news(data_source_id_list=data_source_id_list,
                                             start_time=self.time_dict["yesterday_time"],
                                             end_time=self.time_dict["today_start_time"])['influence']

        today_influence = self._get_news(data_source_id_list=data_source_id_list,
                                         start_time=self.time_dict["today_start_time"],
                                         end_time=self.time_dict["now_time"])['influence']

        day_influence_change = (float(today_influence) - float(yesterday_influence))/float(yesterday_influence)
        day_influence_change = "%.2f" % (day_influence_change * 100) + "%"
        return day_influence_change

    def get_news_objects(self, data_source_id_list, start_time, end_time, sentiment=None):
        """
        获得匹配的新闻或文章对象
        :param data_source_id_list:
        :param start_time:
        :param end_time:
        :param sentiment:
        :return:
        """
        news_objects = self._get_news(data_source_id_list=data_source_id_list,
                                      start_time=start_time,
                                      end_time=end_time,
                                      sentiment=sentiment)['news_objects'].clone()
        return news_objects

    def get_avg_click_repost_read(self, data_source_id_list, start_time, end_time):
        article_objects = self.get_news_objects(data_source_id_list=data_source_id_list,
                                                start_time=start_time,
                                                end_time=end_time)

        article_count = article_objects.count()
        click_count = 0
        repost_count = 0
        avg_click_repost_read_dict = {}
        for article in article_objects:
            click_count += article.get("click_count") if article.get("click_count") else 0
            repost_count += article.get("repost_count") if article.get("repost_count") else 0

        if article_count > 0:
            avg_click_count = float("%.2f" % (float(click_count) / article_count))
            avg_repost_count = float("%.2f" % (float(repost_count) / article_count))

        else:
            avg_click_count = 0
            avg_repost_count = 0

        avg_click_repost_read_dict["avg_click_count"] = avg_click_count
        avg_click_repost_read_dict["avg_repost_count"] = avg_repost_count

        return avg_click_repost_read_dict

    def get_sentiment_statistics_objects(self, data_source_id_list, start_time, end_time):
        sentiment_statistics_objects = self._get_news(data_source_id_list=data_source_id_list,
                                                      start_time=start_time,
                                                      end_time=end_time)["sentiment_statistics"]
        return sentiment_statistics_objects

    def get_sort_news_objects(self, data_source_id_list):
        """
        得到今天按发布时间排序(倒序排列)的对象
        :param data_source_id_list:
        :return:
        """
        contents = {"today_sort_news_objects": self._get_news(data_source_id_list=data_source_id_list,
                                                              start_time=self.time_dict["today_start_time"],
                                                              end_time=self.time_dict["now_time"])["sort_news_objects"],
                    "seven_sort_news_objects": self._get_news(data_source_id_list=data_source_id_list,
                                                              start_time=self.time_dict["seven_ago_time"],
                                                              end_time=self.time_dict["now_time"])["sort_news_objects"]}
        # contents = {"today_sort_news_objects":
        #             self._get_news(data_source_id_list=data_source_id_list,
        #                            start_time="2017-01-03 19:00:00",
        #                            end_time="2017-01-03 19:20:00")["sort_news_objects"]}

        return contents

    def get_news_count(self, data_source_id_list, start_time, end_time):
        """
        获得相应的新闻或文章的数量
        :param data_source_id_list:
        :param start_time:
        :param end_time:
        :return:
        """
        news_count = self._get_news(data_source_id_list, start_time=start_time, end_time=end_time)["news_count"]
        return news_count

    def get_hot_media_objects(self, data_source_id_list):
        """
        7天相关的热门媒体的查找对象新闻或文章数量
        :param data_source_id_list:
        :return:
        """
        if self.__class__.__name__ != "BaiDuZhiDao":
            hot_media_objects = self._get_news(data_source_id_list,
                                               start_time=self.time_dict["seven_ago_time"],
                                               end_time=self.time_dict["now_time"])["hot_media_objects"].clone()
            return hot_media_objects


class BaiDuSearch(BaseSourceMedia):
    """
    百度搜索
    """
    def __init__(self, paras):
        super(BaiDuSearch, self).__init__(paras)
        self._collection_search_baidu = self._db['search_baidu']
        # 百度搜索的影响力比例
        self._influence_scale = 0.2

    def _get_news(self, data_source_id_list, start_time, end_time, sentiment=None):
        """
        新闻影响力和新闻对象
        :param data_source_id_list:
        :param start_time:
        :param end_time:
        :param sentiment:
        :return:
        """
        contents = {}
        if sentiment:
            news_objects = self._collection_search_baidu.find({"$or":
                                                               [{"data_source_id": i} for i in data_source_id_list],
                                                               "sentiment": sentiment,
                                                               "publish_time": {"$gte": start_time, "$lte": end_time}})

            news_count = news_objects.count()
        else:
            news_objects = self._collection_search_baidu.find({"$or":
                                                               [{"data_source_id": i} for i in data_source_id_list],
                                                               "publish_time": {"$gte": start_time, "$lte": end_time}})

            hot_media_objects = self._collection_search_baidu.find({"$or":
                                                                   [{"data_source_id": i} for i in data_source_id_list],
                                                                   "publish_time":
                                                                       {"$gte": start_time, "$lte": end_time}},
                                                                   {"_id": 0, "media": 1})

            sentiment_statistics = self._collection_search_baidu.aggregate([{"$match": {"publish_time":
                                                                                        {"$gte": start_time,
                                                                                         "$lte": end_time}}},
                                                                            {"$group":
                                                                             {"_id": "$sentiment",
                                                                              "count": {"$sum": 1}}}])
            contents["sentiment_statistics"] = sentiment_statistics
            news_count = news_objects.count()
            sort_news_objects = news_objects.sort("-publish_time")
            sort_news_objects_serialize = serialize_news_obj(sort_news_objects)
            hot_media_objects_serialize = serialize_news_obj(hot_media_objects)

            contents["sort_news_objects_serialize"] = sort_news_objects_serialize
            contents["sort_news_objects"] = sort_news_objects
            contents["hot_media_objects_serialize"] = hot_media_objects_serialize
            contents["hot_media_objects"] = hot_media_objects
        news_objects_serialize = serialize_news_obj(news_objects)
        contents["influence"] = self._influence_scale * int(news_count)
        contents["news_objects_serialize"] = news_objects_serialize
        contents["news_objects"] = news_objects
        contents["news_count"] = news_count
        return contents

    def get_object(self, obj_id):
        obj = self._collection_search_baidu.find({"_id": obj_id})
        return obj


class BaiDuTieBa(BaseSourceMedia):
    """
    百度贴吧
    """
    def __init__(self, paras):
        super(BaiDuTieBa, self).__init__(paras)
        self._collection_tieba = self._db['tieba']
        self._collection_tieba_reply = self._db['tieba_reply']
        self._influence_scale = 0.4

    def _get_news(self, data_source_id_list, start_time, end_time, sentiment=None):
        """
        新闻影响力和新闻对象
        :param data_source_id_list:
        :param start_time:
        :param end_time:
        :param sentiment:
        :return:
        """
        contents = {}
        if sentiment:
            news_objects = self._collection_tieba.find({"$or": [{"data_source_id": i} for i in data_source_id_list],
                                                        "sentiment": sentiment,
                                                        "publish_time": {"$gte": start_time, "$lte": end_time}})

            news_count = news_objects.count()
        else:
            news_objects = self._collection_tieba.find({"$or": [{"data_source_id": i} for i in data_source_id_list],
                                                        "publish_time": {"$gte": start_time, "$lte": end_time}})

            hot_media_objects = self._collection_tieba.find({"$or":
                                                            [{"data_source_id": i} for i in data_source_id_list],
                                                            "publish_time": {"$gte": start_time, "$lte": end_time}},
                                                            {"_id": 0, "author": 1})

            sentiment_statistics = self._collection_tieba.aggregate([{"$match": {"publish_time":
                                                                                 {"$gte": start_time,
                                                                                  "$lte": end_time}}},
                                                                    {"$group":
                                                                     {"_id": "$sentiment",
                                                                      "count": {"$sum": 1}}}])
            contents["sentiment_statistics"] = sentiment_statistics

            news_count = news_objects.count()
            sort_news_objects = news_objects.sort("-publish_time")
            sort_news_objects_serialize = serialize_news_obj(sort_news_objects)
            hot_media_objects_serialize = serialize_news_obj(hot_media_objects)

            contents["sort_news_objects_serialize"] = sort_news_objects_serialize
            contents["sort_news_objects"] = sort_news_objects
            contents["hot_media_objects_serialize"] = hot_media_objects_serialize
            contents["hot_media_objects"] = hot_media_objects
        news_objects_serialize = serialize_news_obj(news_objects)
        contents["influence"] = self._influence_scale * int(news_count)
        contents["news_objects_serialize"] = news_objects_serialize
        contents["news_objects"] = news_objects
        contents["news_count"] = news_count
        return contents

    def get_object(self, obj_id):
        obj = self._collection_tieba.find({"_id": obj_id})
        return obj

    def get_reply_obj(self, url):
        obj = self._collection_tieba_reply.find({"url": url})
        return obj


class BaiDuZhiDao(BaseSourceMedia):
    """
    百度知道
    """
    def __init__(self, paras):
        super(BaiDuZhiDao, self).__init__(paras)
        self._collection_zhidao = self._db['zhidao']
        self._collection_zhidao_reply = self._db['zhidao_reply']
        self._influence_scale = 0.3

    def _get_news(self, data_source_id_list, start_time, end_time, sentiment=None):
        """
        新闻影响力和新闻对象
        :param data_source_id_list:
        :param start_time:
        :param end_time:
        :param sentiment:
        :return:
        """
        contents = {}
        if sentiment:
            news_objects = self._collection_zhidao.find({"$or": [{"data_source_id": i} for i in data_source_id_list],
                                                         "sentiment": sentiment,
                                                         "publish_time": {"$gte": start_time, "$lte": end_time}})

            news_count = news_objects.count()
        else:
            news_objects = self._collection_zhidao.find({"$or": [{"data_source_id": i} for i in data_source_id_list],
                                                         "publish_time": {"$gte": start_time, "$lte": end_time}})

            sentiment_statistics = self._collection_zhidao.aggregate([{"$match": {"publish_time":
                                                                                  {"$gte": start_time,
                                                                                   "$lte": end_time}}},
                                                                      {"$group":
                                                                       {"_id": "$sentiment",
                                                                        "count": {"$sum": 1}}}])
            contents["sentiment_statistics"] = sentiment_statistics

            # hot_media_objects = self._collection_zhidao.find({"$or":
            #                                                 [{"data_source_id": i} for i in data_source_id_list],
            #                                                 "publish_time":
            #                                                        {"$gte": start_time, "$lte": end_time}},
            #                                                 {"_id": 0, "author": 1})
            news_count = news_objects.count()
            sort_news_objects = news_objects.sort("-publish_time")
            sort_news_objects_serialize = serialize_news_obj(sort_news_objects)
            # hot_media_objects_serialize = serialize_news_obj(hot_media_objects)

            contents["sort_news_objects_serialize"] = sort_news_objects_serialize
            contents["sort_news_objects"] = sort_news_objects
            # contents["hot_media_objects"] = hot_media_objects_serialize
        news_objects_serialize = serialize_news_obj(news_objects)
        contents["influence"] = self._influence_scale * int(news_count)
        contents["news_objects_serialize"] = news_objects_serialize
        contents["news_objects"] = news_objects
        contents["news_count"] = news_count
        return contents

    def get_object(self, obj_id):
        obj = self._collection_zhidao.find({"_id": obj_id})
        return obj

    def get_reply_obj(self, url):
        obj = self._collection_zhidao_reply.find({"url": url})
        return obj


class WeiBo(BaseSourceMedia):
    """
    微博
    """
    def __init__(self, paras):
        super(WeiBo, self).__init__(paras)
        self._collection_search_weibo = self._db['search_weibo']
        self._collection_weibo_comment = self._db['weibo_comment']
        self._collection_search_weibo_id = self._db['search_weibo_id']
        self._influence_scale = 0.5

    def _get_news(self, data_source_id_list, start_time, end_time, sentiment=None):
        """
        新闻影响力和新闻或文章对象
        :param data_source_id_list:
        :param start_time:
        :param end_time:
        :param sentiment:
        :return:
        """
        contents = {}
        if sentiment:
            news_objects = self._collection_search_weibo.find({"$or":
                                                               [{"data_source_id": i} for i in data_source_id_list],
                                                               "sentiment": sentiment,
                                                               "publish_time": {"$gte": start_time, "$lte": end_time}})

            news_count = news_objects.count()
        else:
            news_objects = self._collection_search_weibo.find({"$or":
                                                               [{"data_source_id": i} for i in data_source_id_list],
                                                               "publish_time": {"$gte": start_time, "$lte": end_time}})

            hot_media_objects = self._collection_search_weibo.find({"$or":
                                                                   [{"data_source_id": i} for i in data_source_id_list],
                                                                   "publish_time":
                                                                       {"$gte": start_time, "$lte": end_time}},
                                                                   {"_id": 0, "author": 1})

            sentiment_statistics = self._collection_search_weibo.aggregate([{"$match": {"publish_time":
                                                                                        {"$gte": start_time,
                                                                                         "$lte": end_time}}},
                                                                            {"$group":
                                                                             {"_id": "$sentiment",
                                                                              "count": {"$sum": 1}}}])
            contents["sentiment_statistics"] = sentiment_statistics

            news_count = news_objects.count()
            sort_news_objects = news_objects.sort("-publish_time")
            sort_news_objects_serialize = serialize_news_obj(sort_news_objects)
            hot_media_objects_serialize = serialize_news_obj(hot_media_objects)

            contents["sort_news_objects_serialize"] = sort_news_objects_serialize
            contents["sort_news_objects"] = sort_news_objects
            contents["hot_media_objects_serialize"] = hot_media_objects_serialize
            contents["hot_media_objects"] = hot_media_objects
        news_objects_serialize = serialize_news_obj(news_objects)
        contents["influence"] = self._influence_scale * int(news_count)
        contents["news_objects_serialize"] = news_objects_serialize
        contents["news_objects"] = news_objects
        contents["news_count"] = news_count
        return contents

    def get_weibo_comment_location(self, data_source_id_list):
        start_time = self.time_dict["seven_ago_time"]
        end_time = self.time_dict["now_time"]

        weibo_comment_location_objects = self._collection_weibo_comment.find({"$or":
                                                                             [{"data_source_id": i}
                                                                              for i in data_source_id_list],
                                                                              "comment_time": {
                                                                                "$gte": start_time, "$lte": end_time}},
                                                                             {"_id": 0, "country": 1,
                                                                              "zone": 1, "city": 1})
        return weibo_comment_location_objects

    def get_search_weibo_id_info(self, data_source_id_list):
        pass

    def get_object(self, obj_id):
        obj = self._collection_search_weibo.find({"_id": obj_id})
        return obj

    def get_comment_obj(self, weibo_id):
        obj = self._collection_weibo_comment.find({"weibo_id": weibo_id})
        return obj


class WeiXin(BaseSourceMedia):
    """
    微信
    """
    def __init__(self, paras):
        super(WeiXin, self).__init__(paras)
        self._collection_weixin_article = self._db['weixin_article']
        self._collection_weixin_id_info = self._db['weixin_id_info']
        self._influence_scale = 0.6

    def _get_news(self, data_source_id_list, start_time, end_time, sentiment=None):
        """
        新闻影响力和新闻或文章对象
        :param data_source_id_list:
        :param start_time:
        :param end_time:
        :param sentiment:
        :return:
        """
        contents = {}
        if sentiment:
            news_objects = self._collection_weixin_article.find({"$or":
                                                                 [{"data_source_id": i} for i in data_source_id_list],
                                                                 "sentiment": sentiment,
                                                                 "publish_time": {"$gte": start_time,
                                                                                  "$lte": end_time}})

            news_count = news_objects.count()
        else:
            news_objects = self._collection_weixin_article.find({"$or":
                                                                 [{"data_source_id": i} for i in data_source_id_list],
                                                                 "publish_time": {"$gte": start_time,
                                                                                  "$lte": end_time}})

            hot_media_objects = self._collection_weixin_article.find({"$or":
                                                                     [{"data_source_id": i}
                                                                      for i in data_source_id_list],
                                                                     "publish_time":
                                                                         {"$gte": start_time, "$lte": end_time}},
                                                                     {"_id": 0, "author": 1})

            sentiment_statistics = self._collection_weixin_article.aggregate([{"$match": {"publish_time":
                                                                                          {"$gte": start_time,
                                                                                           "$lte": end_time}}},
                                                                              {"$group":
                                                                              {"_id": "$sentiment",
                                                                               "count": {"$sum": 1}}}])

            contents["sentiment_statistics"] = sentiment_statistics
            news_count = news_objects.count()
            sort_news_objects = news_objects.sort("-publish_time")
            sort_news_objects_serialize = serialize_news_obj(sort_news_objects)
            hot_media_objects_serialize = serialize_news_obj(hot_media_objects)

            contents["sort_news_objects_serialize"] = sort_news_objects_serialize
            contents["sort_news_objects"] = sort_news_objects
            contents["hot_media_objects_serialize"] = hot_media_objects_serialize
            contents["hot_media_objects"] = hot_media_objects
        news_objects_serialize = serialize_news_obj(news_objects)
        contents["influence"] = self._influence_scale * int(news_count)
        contents["news_objects_serialize"] = news_objects_serialize
        contents["news_objects"] = news_objects
        contents["news_count"] = news_count
        return contents

    def get_object(self, obj_id):
        obj = self._collection_weixin_article.find({"_id": obj_id})
        return obj


class ZhiHu(BaseSourceMedia):
    """
    知乎
    """
    def __init__(self, paras):
        super(ZhiHu, self).__init__(paras)
        self._collection_zhihu = self._db['zhihu']
        self._influence_scale = 0.3

    def _get_news(self, data_source_id_list, start_time, end_time, sentiment=None):
        """
        新闻影响力和新闻或文章对象
        :param data_source_id_list:
        :param start_time:
        :param end_time:
        :param sentiment:
        :return:
        """
        contents = {}
        if sentiment:
            news_objects = self._collection_zhihu.find({"$or":
                                                        [{"data_source_id": i} for i in data_source_id_list],
                                                        "sentiment": sentiment,
                                                        "publish_time": {"$gte": start_time, "$lte": end_time}})

            news_count = news_objects.count()
        else:
            news_objects = self._collection_zhihu.find({"$or":
                                                        [{"data_source_id": i} for i in data_source_id_list],
                                                        "publish_time": {"$gte": start_time, "$lte": end_time}})

            hot_media_objects = self._collection_zhihu.find({"$or":
                                                            [{"data_source_id": i} for i in data_source_id_list],
                                                            "publish_time":
                                                                {"$gte": start_time, "$lte": end_time}},
                                                            {"_id": 0, "media": 1})

            sentiment_statistics = self._collection_zhihu.aggregate([{"$match": {"publish_time":
                                                                                 {"$gte": start_time,
                                                                                  "$lte": end_time}}},
                                                                     {"$group":
                                                                     {"_id": "$sentiment",
                                                                      "count": {"$sum": 1}}}])
            contents["sentiment_statistics"] = sentiment_statistics

            news_count = news_objects.count()
            sort_news_objects = news_objects.sort("-publish_time")
            sort_news_objects_serialize = serialize_news_obj(sort_news_objects)
            hot_media_objects_serialize = serialize_news_obj(hot_media_objects)

            contents["sort_news_objects_serialize"] = sort_news_objects_serialize
            contents["sort_news_objects"] = sort_news_objects
            contents["hot_media_objects_serialize"] = hot_media_objects_serialize
            contents["hot_media_objects"] = hot_media_objects
        news_objects_serialize = serialize_news_obj(news_objects)
        contents["influence"] = self._influence_scale * int(news_count)
        contents["news_objects_serialize"] = news_objects_serialize
        contents["news_objects"] = news_objects
        contents["news_count"] = news_count
        return contents

    def get_object(self, obj_id):
        obj = self._collection_zhihu.find({"_id": obj_id})
        return obj


class AppStore(object):
    """
    苹果应用商店
    """
    def __init__(self, paras):
        self._db = get_mongodb_client(paras)['sem_test']
        self.time_dict = get_time()
        self._collection_app_comments = self._db['app_comments']
        self._collection_app_detail = self._db['app_detail']
        self._collection_app_bangdan = self._db['app_bangdan']
        self._influence_scale = 0

    def get_app_comments_info(self, data_source_id_list):
        """
        新闻影响力和新闻对象
        :param data_source_id_list:
        :return:
        """
        app_comments_info = {}
        comments_objects = self._collection_app_comments.find({"$or":
                                                              [{"data_source_id": i} for i in data_source_id_list]})
        # comments_objects = self._collection_app_comments.find({"appid": "938688461"})
        # dif_sentiment_count = self._collection_app_comments.aggregate(
        #     [{"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}])
        sentiment_count_dict = {"negative_count": 0, "positive_count": 0, "neutral_count": 0}
        sentiment_obj_dict = {"negative_obj": [], "positive_obj": [], "neutral_obj": []}
        rating_count_dict = {"1星": 0, "2星": 0, "3星": 0, "4星": 0, "5星": 0}
        rating_obj_dict = {"1星": [], "2星": [], "3星": [], "4星": [], "5星": []}
        sort_comments_objects = comments_objects.sort("-publish_time").limit(100)
        for obj in sort_comments_objects:
            # 不同情感值评论的数量
            sentiment = obj.get("comment_sentiment") if obj.get("comment_sentiment") else 0
            if sentiment == "negative":
                sentiment_count_dict["negative_count"] += 1
                sentiment_obj_dict["negative_obj"].append(serialize_news_obj(obj))
            elif sentiment == "positive":
                sentiment_count_dict["positive_count"] += 1
                sentiment_obj_dict["positive_obj"].append(serialize_news_obj(obj))
            elif sentiment == "neutral":
                sentiment_count_dict["neutral_count"] += 1
                sentiment_obj_dict["neutral_obj"].append(serialize_news_obj(obj))

            # 不同评分的评论的数量
            if obj["rating"] == 1:
                rating_count_dict["1星"] += 1
                rating_obj_dict["1星"].append(serialize_news_obj(obj))
            elif obj["rating"] == 2:
                rating_count_dict["2星"] += 1
                rating_obj_dict["2星"].append(serialize_news_obj(obj))
            elif obj["rating"] == 3:
                rating_count_dict["3星"] += 1
                rating_obj_dict["3星"].append(serialize_news_obj(obj))
            elif obj["rating"] == 4:
                rating_count_dict["4星"] += 1
                rating_obj_dict["4星"].append(serialize_news_obj(obj))
            elif obj["rating"] == 5:
                rating_count_dict["5星"] += 1
                rating_obj_dict["5星"].append(serialize_news_obj(obj))

        app_comments_info["sort_comments_objects"] = serialize_news_obj(sort_comments_objects.clone())
        app_comments_info["sentiment_count_dict"] = sentiment_count_dict
        app_comments_info["rating_count_dict"] = rating_count_dict
        app_comments_info["sentiment_obj_dict"] = sentiment_obj_dict
        app_comments_info["rating_obj_dict"] = rating_obj_dict
        return app_comments_info

    def get_app_bangdan_info_obj(self, data_source_id_list):
        """
        得到app榜单collection中的数据
        :param data_source_id_list:
        :return:
        """
        app_bangdan_info_obj = self._collection_app_bangdan.find({"$or":
                                                                 [{"data_source_id": i} for i in data_source_id_list]})
        return serialize_news_obj(app_bangdan_info_obj)

    def get_app_detail_obj(self, data_source_id_list):
        """
        得到app详情collection中的数据
        :param data_source_id_list:
        :return:
        """
        app_detail_obj = self._collection_app_detail.find({"$or":
                                                          [{"data_source_id": i} for i in data_source_id_list]})
        return serialize_news_obj(app_detail_obj)


if __name__ == "__main__":
    pass
