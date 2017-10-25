# -*- coding:utf-8 -*-

from settings import get_mongodb_client, INFL_SCALE, DB
from common import get_time, seria_news_obj


class BaseSourceMedia(object):

    def __init__(self, paras):
        """
        连接到指定的mongodb数据库
        """
        self._db = get_mongodb_client(paras)[DB]
        self.time_dict = get_time()
        self.infl_scale = 0

    def _get_news(self, data_sour_id_list, start_time, end_time, sent=None):
        """
        新闻影响力和新闻对象
        :param data_sour_id_list:
        :param start_time:
        :param end_time:
        :param sent:
        :return:
        """
        return {}

    def get_infl(self, data_sour_id_list, start_time=None, end_time=None):
        """
        最近7天、上个7天、今天、昨天的影响力
        :param end_time:
        :param start_time:
        :param data_sour_id_list:
        :return:
        """
        infl_dict = {}
        if start_time and end_time:
            usr_def_infl = self.get_news_count(data_sour_id_list=data_sour_id_list,
                                               start_time=start_time,
                                               end_time=end_time) * self.infl_scale
            infl_dict["usr_def_infl"] = round(usr_def_infl, 2)
        else:
            sev_infl = self.get_news_count(data_sour_id_list=data_sour_id_list,
                                           start_time=self.time_dict["sev_ago_time"],
                                           end_time=self.time_dict["now_time"]) * self.infl_scale

            last_sev_infl = self.get_news_count(data_sour_id_list=data_sour_id_list,
                                                start_time=self.time_dict["fourteen_ago_time"],
                                                end_time=self.time_dict["sev_ago_time"]) * self.infl_scale

            tod_infl = self.get_news_count(data_sour_id_list=data_sour_id_list,
                                           start_time=self.time_dict["tod_start_time"],
                                           end_time=self.time_dict["now_time"]) * self.infl_scale

            yest_infl = self.get_news_count(data_sour_id_list=data_sour_id_list,
                                            start_time=self.time_dict["yest_time"],
                                            end_time=self.time_dict["tod_start_time"]) * self.infl_scale

            infl_dict["sev_infl"] = round(sev_infl, 2)
            infl_dict["last_sev_infl"] = round(last_sev_infl, 2)
            infl_dict["tod_infl"] = round(tod_infl, 2)
            infl_dict["yest_infl"] = round(yest_infl, 2)

        return infl_dict

    def get_sent_infl(self, data_sour_id_list, start_time=None, end_time=None):
        """
        根据情感值分别得到不同情感值的影响力
        :param end_time:
        :param start_time:
        :param data_sour_id_list:
        :return:
        """
        sent_infl_dict = {}  # 存储不同时间段、不同情感值的影响力
        tod_sent_infl_dict = {}
        yest_sent_infl_dict = {}
        sev_sent_infl_dict = {}
        usr_def_sent_infl_dict = {}
        sent_list = ['negative', 'positive', 'neutral']

        for sent in sent_list:
            if start_time and end_time:
                usr_def_sent_infl = self.get_news_count(data_sour_id_list=data_sour_id_list,
                                                        start_time=start_time,
                                                        end_time=end_time,
                                                        sent=sent) * self.infl_scale
                usr_def_sent_infl_dict[sent] = round(usr_def_sent_infl, 2)
            else:
                tod_sent_infl = self.get_news_count(data_sour_id_list=data_sour_id_list,
                                                    start_time=self.time_dict["tod_start_time"],
                                                    end_time=self.time_dict["now_time"],
                                                    sent=sent) * self.infl_scale
                
                yest_sent_infl = self.get_news_count(data_sour_id_list=data_sour_id_list,
                                                     start_time=self.time_dict["tod_start_time"],
                                                     end_time=self.time_dict["now_time"],
                                                     sent=sent) * self.infl_scale
                
                sev_sent_infl = self.get_news_count(data_sour_id_list=data_sour_id_list,
                                                    start_time=self.time_dict["sev_ago_time"],
                                                    end_time=self.time_dict["now_time"],
                                                    sent=sent) * self.infl_scale

                tod_sent_infl_dict[sent] = round(tod_sent_infl, 2)
                yest_sent_infl_dict[sent] = round(yest_sent_infl, 2)
                sev_sent_infl_dict[sent] = round(sev_sent_infl, 2)

        if start_time and end_time:
            sent_infl_dict["usr_def_sent_infl_dict"] = usr_def_sent_infl_dict
        else:
            sent_infl_dict["tod_sent_infl_dict"] = tod_sent_infl_dict
            sent_infl_dict["yest_sent_infl_dict"] = yest_sent_infl_dict
            sent_infl_dict["sev_sent_infl_dict"] = sev_sent_infl_dict
        return sent_infl_dict

    def get_week_infl_chg(self, data_sour_id_list):
        """
        本周与上周影响力的对比
        :param data_sour_id_list:
        :return:
        """
        last_week_infl = self.get_news_count(data_sour_id_list=data_sour_id_list,
                                             start_time=self.time_dict["fourteen_ago_time"],
                                             end_time=self.time_dict["sev_ago_time"]) * self.infl_scale
        cur_week_infl = self.get_news_count(data_sour_id_list=data_sour_id_list,
                                            start_time=self.time_dict["sev_ago_time"],
                                            end_time=self.time_dict["now_time"]) * self.infl_scale

        week_infl_chg = (float(cur_week_infl) - float(last_week_infl))/float(last_week_infl)
        week_infl_chg = "%.2f" % (week_infl_chg * 100) + "%"
        return week_infl_chg

    def get_day_infl_chg(self, data_sour_id_list):
        """
        单个数据源的今天与昨天影响力对比
        :param data_sour_id_list:
        :return:
        """

        yest_infl = self.get_news_count(data_sour_id_list=data_sour_id_list,
                                        start_time=self.time_dict["yest_time"],
                                        end_time=self.time_dict["tod_start_time"]) * self.infl_scale

        tod_infl = self.get_news_count(data_sour_id_list=data_sour_id_list,
                                       start_time=self.time_dict["tod_start_time"],
                                       end_time=self.time_dict["now_time"]) * self.infl_scale

        day_infl_chg = (float(tod_infl) - float(yest_infl))/float(yest_infl)
        day_infl_chg = "%.2f" % (day_infl_chg * 100) + "%"
        return day_infl_chg

    def get_news_objs(self, data_sour_id_list, start_time, end_time, sent=None):
        """
        获得匹配的新闻或文章对象
        :param data_sour_id_list:
        :param start_time:
        :param end_time:
        :param sent:
        :return:
        """
        news_objs = self._get_news(data_sour_id_list=data_sour_id_list,
                                   start_time=start_time,
                                   end_time=end_time,
                                   sent=sent)['news_objs'].clone()
        return news_objs

    def get_news_count(self, data_sour_id_list, start_time, end_time, sent=None):
        """
        获得相应的新闻或文章的数量
        :param sent:
        :param data_sour_id_list:
        :param start_time:
        :param end_time:
        :return:
        """
        news_obj = self._get_news(data_sour_id_list,
                                  start_time=start_time,
                                  end_time=end_time,
                                  sent=sent)["news_objs"]
        news_count = news_obj.count()
        return news_count

    def get_avg_cli_rep_comt_dict(self, data_sour_id_list, start_time, end_time):
        art_objs = self.get_news_objs(data_sour_id_list=data_sour_id_list,
                                      start_time=start_time, end_time=end_time)

        art_count = art_objs.count()
        cli_count = 0
        rep_count = 0
        comt_count = 0

        contents = {}
        for art in art_objs:
            cli_count += art.get("click_count") if art.get("click_count") else 0
            rep_count += art.get("repost_count") if art.get("repost_count") else 0
            comt_count += art.get("comment_count") if art.get("comment_count") else 0

        if art_count > 0:
            avg_cli_count = float("%.2f" % (float(cli_count) / art_count))
            avg_rep_count = float("%.2f" % (float(rep_count) / art_count))
            avg_comt_count = float("%.2f" % (float(comt_count) / art_count))

        else:
            avg_cli_count = 0
            avg_rep_count = 0
            avg_comt_count = 0

        contents["avg_cli_count"] = avg_cli_count
        contents["avg_rep_count"] = avg_rep_count
        contents["avg_comt_count"] = avg_comt_count
        contents["art_count"] = art_count
        return contents

    # def get_sent_stas_objs(self, data_sour_id_list, start_time, end_time):
    #     sent_stas_objs = self.get_sent_stas_objs(data_sour_id_list=data_sour_id_list,
    #                                              start_time=start_time,
    #                                              end_time=end_time)
    #     return sent_stas_objs

    def get_sort_news_objs(self, data_sour_id_list):
        """
        得到今天按发布时间排序(倒序排列)的对象
        :param data_sour_id_list:
        :return:
        """
        tod_news_obj = self._get_news(data_sour_id_list=data_sour_id_list,
                                      start_time=self.time_dict["tod_start_time"],
                                      end_time=self.time_dict["now_time"])["news_objs"]
        sev_news_obj = self._get_news(data_sour_id_list=data_sour_id_list,
                                      start_time=self.time_dict["sev_ago_time"],
                                      end_time=self.time_dict["now_time"])["news_objs"]

        contents = {
            "tod_sort_news_objs": tod_news_obj.sort("-publish_time"),
            "sev_sort_news_objs": sev_news_obj.sort("-publish_time")
        }

        return contents

    def get_hot_med_objs(self, data_sour_id_list):
        """
        7天相关的热门媒体的查找对象新闻或文章数量
        :param data_sour_id_list:
        :return:
        """
        if self.__class__.__name__ != "BaiDuZhiDao":
            hot_med_objs = self._get_news(data_sour_id_list,
                                          start_time=self.time_dict["sev_ago_time"],
                                          end_time=self.time_dict["now_time"])["hot_med_objs"].clone()
            return hot_med_objs


class BaiDuSearch(BaseSourceMedia):
    """
    百度搜索
    """
    def __init__(self, paras):
        super(BaiDuSearch, self).__init__(paras)
        self._coll_search_baidu = self._db['search_baidu']
        # 百度搜索的影响力比例
        self.infl_scale = INFL_SCALE["baidu_search"]

    def _get_news(self, data_sour_id_list, start_time, end_time, sent=None):
        """
        新闻影响力和新闻对象
        :param data_sour_id_list:
        :param start_time:
        :param end_time:
        :param sent:
        :return:
        """
        contents = {}
        if sent:
            news_objs = self._coll_search_baidu.find({"$or":
                                                      [{"data_source_id": i} for i in data_sour_id_list],
                                                      "sentiment": sent,
                                                      "publish_time": {"$gte": start_time, "$lte": end_time}})

        else:
            news_objs = self._coll_search_baidu.find({"$or":
                                                     [{"data_source_id": i} for i in data_sour_id_list],
                                                      "publish_time": {"$gte": start_time, "$lte": end_time}},
                                                     {
                                                         "_id": 1,
                                                         "title": 1,
                                                         "main_body": 1,
                                                         "publish_time": 1,
                                                         "data_type": 1,
                                                         "sentiment": 1,
                                                         "data_media": 1,
                                                     })

        contents["news_objs"] = news_objs
        return contents

    def get_obj(self, obj_id):
        obj = self._coll_search_baidu.find({"_id": obj_id})
        return obj

    def get_hot_med_obj(self, data_sour_id_list, start_time, end_time):
        hot_med_obj = self._coll_search_baidu.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                                    "publish_time": {"$gte": start_time, "$lte": end_time}},
                                                   {"_id": 0, "med": 1})
        return hot_med_obj

    def get_sent_stas(self, data_sour_id_list, start_time, end_time):
        sent_stas = self._coll_search_baidu.aggregate([{"$match":
                                                       {"publish_time": {"$gte": start_time, "$lte": end_time}}},
                                                       {"$match": {"$or": [{"data_source_id": i} 
                                                                           for i in data_sour_id_list]}},
                                                       {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}])
        return sent_stas


class BaiDuTieBa(BaseSourceMedia):
    """
    百度贴吧
    """
    def __init__(self, paras):
        super(BaiDuTieBa, self).__init__(paras)
        self._coll_tieba = self._db['tieba']
        self._coll_tieba_reply = self._db['tieba_reply']
        self.infl_scale = INFL_SCALE["baidu_tieba"]

    def _get_news(self, data_sour_id_list, start_time, end_time, sent=None):
        """
        新闻影响力和新闻对象
        :param data_sour_id_list:
        :param start_time:
        :param end_time:
        :param sent:
        :return:
        """
        contents = {}
        if sent:
            news_objs = self._coll_tieba.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                               "sentiment": sent,
                                               "publish_time": {"$gte": start_time, "$lte": end_time}})

        else:
            news_objs = self._coll_tieba.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                               "publish_time": {"$gte": start_time, "$lte": end_time}},
                                              {
                                                  "_id": 1,
                                                  "title": 1,
                                                  "main_body": 1,
                                                  "publish_time": 1,
                                                  "data_type": 1,
                                                  "sentiment": 1,
                                                  "data_media": 1,
                                              })

        contents["news_objs"] = news_objs
        return contents

    def get_obj(self, obj_id):
        obj = self._coll_tieba.find({"_id": obj_id})
        return obj

    def get_reply_obj(self, url):
        obj = self._coll_tieba_reply.find({"url": url})
        return obj

    def get_hot_med_obj(self, data_sour_id_list, start_time, end_time):
        hot_med_obj = self._coll_tieba.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                            "publish_time": {"$gte": start_time, "$lte": end_time}},
                                            {"_id": 0, "author": 1})
        return hot_med_obj

    def get_sent_stas(self, data_sour_id_list, start_time, end_time):
        sent_stas = self._coll_tieba.aggregate([{"$match": {"publish_time": {"$gte": start_time, "$lte": end_time}}},
                                                {"$match": {"$or": [{"data_source_id": i} 
                                                                    for i in data_sour_id_list]}},
                                                {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}])
        return sent_stas


class BaiDuZhiDao(BaseSourceMedia):
    """
    百度知道
    """
    def __init__(self, paras):
        super(BaiDuZhiDao, self).__init__(paras)
        self._coll_zhidao = self._db['zhidao']
        self._coll_zhidao_reply = self._db['zhidao_reply']
        self.infl_scale = INFL_SCALE["baidu_zhidao"]

    def _get_news(self, data_sour_id_list, start_time, end_time, sent=None):
        """
        新闻影响力和新闻对象
        :param data_sour_id_list:
        :param start_time:
        :param end_time:
        :param sent:
        :return:
        """
        contents = {}
        if sent:
            news_objs = self._coll_zhidao.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                                "sentiment": sent,
                                                "publish_time": {"$gte": start_time, "$lte": end_time}})

        else:
            news_objs = self._coll_zhidao.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                                "publish_time": {"$gte": start_time, "$lte": end_time}},
                                               {
                                                   "_id": 1,
                                                   "title": 1,
                                                   "main_body": 1,
                                                   "publish_time": 1,
                                                   "data_type": 1,
                                                   "sentiment": 1,
                                                   "data_media": 1,
                                               })

        contents["news_objs"] = news_objs
        return contents

    def get_obj(self, obj_id):
        obj = self._coll_zhidao.find({"_id": obj_id})
        return obj

    def get_reply_obj(self, url):
        obj = self._coll_zhidao_reply.find({"url": url})
        return obj

    def get_hot_med_obj(self, data_sour_id_list, start_time, end_time):
        hot_med_obj = self._coll_zhidao.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                             "publish_time": {"$gte": start_time, "$lte": end_time}},
                                             {"_id": 0, "med": 1})
        return hot_med_obj

    def get_sent_stas(self, data_sour_id_list, start_time, end_time):
        sent_stas = self._coll_zhidao.aggregate([{"$match": {"publish_time": {"$gte": start_time, "$lte": end_time}}},
                                                 {"$match": {"$or": [{"data_source_id": i}
                                                                     for i in data_sour_id_list]}},
                                                 {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}])
        return sent_stas


class WeiBo(BaseSourceMedia):
    """
    微博
    """
    def __init__(self, paras):
        super(WeiBo, self).__init__(paras)
        self._coll_search_weibo = self._db['search_weibo']
        self._coll_weibo_comt = self._db['weibo_comment']
        self._coll_search_weibo_id = self._db['search_weibo_id']
        self.infl_scale = INFL_SCALE["weibo"]

    def _get_news(self, data_sour_id_list, start_time, end_time, sent=None):
        """
        新闻影响力和新闻或文章对象
        :param data_sour_id_list:
        :param start_time:
        :param end_time:
        :param sent:
        :return:
        """
        contents = {}
        if sent:
            news_objs = self._coll_search_weibo.find({"$or":
                                                     [{"data_source_id": i} for i in data_sour_id_list],
                                                      "sentiment": sent,
                                                      "publish_time": {"$gte": start_time, "$lte": end_time}})

        else:
            news_objs = self._coll_search_weibo.find({"$or":
                                                     [{"data_source_id": i} for i in data_sour_id_list],
                                                     "publish_time": {"$gte": start_time, "$lte": end_time}},
                                                     {
                                                         "_id": 1,
                                                         "title": 1,
                                                         "main_body": 1,
                                                         "publish_time": 1,
                                                         "data_type": 1,
                                                         "sentiment": 1,
                                                         "data_media": 1,
                                                         "click_count": 1,
                                                         "repost_count": 1,
                                                         "comment_count": 1,
                                                     })

        contents["news_objs"] = news_objs
        return contents

    def get_weibo_comt_loc(self, data_sour_id_list, start_time, end_time):
        weibo_comt_loc_objs = self._coll_weibo_comt.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                                          "comment_time": {"$gte": start_time, "$lte": end_time}},
                                                         {"_id": 0, "country": 1, "zone": 1, "city": 1})
        return weibo_comt_loc_objs

    def get_search_weibo_id_info(self, data_sour_id_list):
        pass

    def get_obj(self, obj_id):
        obj = self._coll_search_weibo.find({"_id": obj_id})
        return obj

    def get_comt_obj(self, weibo_id):
        obj = self._coll_weibo_comt.find({"weibo_id": weibo_id})
        return obj

    def get_hot_med_obj(self, data_sour_id_list, start_time, end_time):
        hot_med_obj = self._coll_search_weibo.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                                    "publish_time": {"$gte": start_time, "$lte": end_time}},
                                                   {"_id": 0, "med": 1})
        return hot_med_obj

    def get_sent_stas(self, data_sour_id_list, start_time, end_time):
        sent_stas = self._coll_search_weibo.aggregate([{"$match": {"publish_time": {"$gte": start_time,
                                                                                    "$lte": end_time}}},
                                                       {"$match": {"$or": [{"data_source_id": i}
                                                                           for i in data_sour_id_list]}},
                                                       {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}])
        return sent_stas


class WeiXin(BaseSourceMedia):
    """
    微信
    """
    def __init__(self, paras):
        super(WeiXin, self).__init__(paras)
        self._coll_weixin_art = self._db['weixin_article']
        self._coll_weixin_id_info = self._db['weixin_id_info']
        self.infl_scale = INFL_SCALE["weixin"]

    def _get_news(self, data_sour_id_list, start_time, end_time, sent=None):
        """
        新闻影响力和新闻或文章对象
        :param data_sour_id_list:
        :param start_time:
        :param end_time:
        :param sent:
        :return:
        """
        contents = {}
        if sent:
            news_objs = self._coll_weixin_art.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                                    "sentiment": sent,
                                                    "publish_time": {"$gte": start_time, "$lte": end_time}})

        else:
            news_objs = self._coll_weixin_art.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                                    "publish_time": {"$gte": start_time, "$lte": end_time}},
                                                   {
                                                       "_id": 1,
                                                       "title": 1,
                                                       "main_body": 1,
                                                       "publish_time": 1,
                                                       "data_type": 1,
                                                       "sentiment": 1,
                                                       "data_media": 1,
                                                       "click_count": 1,
                                                       "repost_count": 1,
                                                       "comment_count": 1,
                                                   })

        contents["news_objs"] = news_objs
        return contents

    def get_obj(self, obj_id):
        obj = self._coll_weixin_art.find({"_id": obj_id})
        return obj

    def get_hot_med_obj(self, data_sour_id_list, start_time, end_time):
        hot_med_obj = self._coll_weixin_art.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                                  "publish_time": {"$gte": start_time, "$lte": end_time}},
                                                 {"_id": 0, "med": 1})
        return hot_med_obj

    def get_sent_stas(self, data_sour_id_list, start_time, end_time):
        sent_stas = self._coll_weixin_art.aggregate([{"$match":
                                                     {"publish_time": {"$gte": start_time,
                                                                       "$lte": end_time}}},
                                                     {"$match": {"$or": [{"data_source_id": i}
                                                                 for i in data_sour_id_list]}},
                                                     {"$group": {"_id": "$sentiment",
                                                                 "count": {"$sum": 1}}}])
        return sent_stas


class ZhiHu(BaseSourceMedia):
    """
    知乎
    """
    def __init__(self, paras):
        super(ZhiHu, self).__init__(paras)
        self._coll_zhihu = self._db['zhihu']
        self.infl_scale = INFL_SCALE["zhihu"]

    def _get_news(self, data_sour_id_list, start_time, end_time, sent=None):
        """
        新闻影响力和新闻或文章对象
        :param data_sour_id_list:
        :param start_time:
        :param end_time:
        :param sent:
        :return:
        """
        contents = {}
        if sent:
            news_objs = self._coll_zhihu.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                               "sentiment": sent,
                                               "publish_time": {"$gte": start_time, "$lte": end_time}})

        else:
            news_objs = self._coll_zhihu.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                               "publish_time": {"$gte": start_time, "$lte": end_time}},
                                              {
                                                  "_id": 1,
                                                  "title": 1,
                                                  "main_body": 1,
                                                  "publish_time": 1,
                                                  "data_type": 1,
                                                  "sentiment": 1,
                                                  "data_media": 1,
                                              })

        contents["news_objs"] = news_objs
        return contents

    def get_obj(self, obj_id):
        obj = self._coll_zhihu.find({"_id": obj_id})
        return obj

    def get_hot_med_obj(self, data_sour_id_list, start_time, end_time):
        hot_med_obj = self._coll_zhihu.find({"$or": [{"data_source_id": i} for i in data_sour_id_list],
                                             "publish_time": {"$gte": start_time, "$lte": end_time}},
                                            {"_id": 0, "med": 1})
        return hot_med_obj

    def get_sent_stas(self, data_sour_id_list, start_time, end_time):
        sent_stas = self._coll_zhihu.aggregate([{"$match": {"publish_time": {"$gte": start_time, "$lte": end_time}}},
                                                {"$match": {"$or": [{"data_source_id": i}
                                                                    for i in data_sour_id_list]}},
                                                {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}])
        return sent_stas


class AppStore(object):
    """
    苹果应用商店
    """
    def __init__(self, paras):
        self._db = get_mongodb_client(paras)[DB]
        self.time_dict = get_time()
        self._coll_app_comts = self._db['app_comments']
        self._coll_app_det = self._db['app_detail']
        self._coll_app_bd = self._db['app_bangdan']

    def get_app_comts_info(self, data_sour_id_list):
        """
        新闻影响力和新闻对象
        :param data_sour_id_list:
        :return:
        """
        app_comts_info = {}
        comts_objs = self._coll_app_comts.find({"$or": [{"data_source_id": i} for i in data_sour_id_list]})
        # dif_sent_count = self._coll_app_comts.aggregate(
        #     [{"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}])
        sent_count_dict = {"neg_count": 0, "pos_count": 0, "neu_count": 0}
        sent_obj_dict = {"neg_obj": [], "pos_obj": [], "neu_obj": []}
        rating_count_dict = {"1星": 0, "2星": 0, "3星": 0, "4星": 0, "5星": 0}
        rating_obj_dict = {"1星": [], "2星": [], "3星": [], "4星": [], "5星": []}
        sort_comts_objs = comts_objs.sort("-publish_time").limit(100)
        for obj in sort_comts_objs:
            # 不同情感值评论的数量
            sent = obj.get("comment_sentiment") if obj.get("comment_sentiment") else 0
            if sent == "negative":
                sent_count_dict["neg_count"] += 1
                sent_obj_dict["neg_obj"].append(seria_news_obj(obj))
            elif sent == "positive":
                sent_count_dict["pos_count"] += 1
                sent_obj_dict["pos_obj"].append(seria_news_obj(obj))
            elif sent == "neutral":
                sent_count_dict["neu_count"] += 1
                sent_obj_dict["neu_obj"].append(seria_news_obj(obj))

            # 不同评分的评论的数量
            if obj["rating"] == 1:
                rating_count_dict["1星"] += 1
                rating_obj_dict["1星"].append(seria_news_obj(obj))
            elif obj["rating"] == 2:
                rating_count_dict["2星"] += 1
                rating_obj_dict["2星"].append(seria_news_obj(obj))
            elif obj["rating"] == 3:
                rating_count_dict["3星"] += 1
                rating_obj_dict["3星"].append(seria_news_obj(obj))
            elif obj["rating"] == 4:
                rating_count_dict["4星"] += 1
                rating_obj_dict["4星"].append(seria_news_obj(obj))
            elif obj["rating"] == 5:
                rating_count_dict["5星"] += 1
                rating_obj_dict["5星"].append(seria_news_obj(obj))

        app_comts_info["sort_comts_objs"] = seria_news_obj(sort_comts_objs.clone())
        app_comts_info["sent_count_dict"] = sent_count_dict
        app_comts_info["rating_count_dict"] = rating_count_dict
        app_comts_info["sent_obj_dict"] = sent_obj_dict
        app_comts_info["rating_obj_dict"] = rating_obj_dict
        return app_comts_info

    def get_app_bd_info_obj(self, data_sour_id_list):
        """
        得到app榜单coll中的数据
        :param data_sour_id_list:
        :return:
        """
        app_bd_info_obj = self._coll_app_bd.find({"$or": [{"data_source_id": i} for i in data_sour_id_list]})
        return seria_news_obj(app_bd_info_obj)

    def get_app_det_obj(self, data_sour_id_list):
        """
        得到app详情coll中的数据
        :param data_sour_id_list:
        :return:
        """
        app_det_obj = self._coll_app_det.find({"$or": [{"data_source_id": i} for i in data_sour_id_list]})
        return seria_news_obj(app_det_obj)


if __name__ == "__main__":
    pass
