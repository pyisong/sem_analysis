# *-* coding:utf-8 *-*

from django.db import models

# Create your models here.


class AdminUserInfo(models.Model):

    UserState = (
        ("0", '停用'),
        ("1", '启用'),
    )
    IsDel = (
        ("0", '否'),
        ("1", '是'),
    )

    user_id = models.AutoField(verbose_name="用户ID", primary_key=True)
    user_name = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    true_name = models.CharField(verbose_name="真实姓名", max_length=32)
    email = models.CharField(verbose_name="邮箱", max_length=32)
    mobile = models.CharField(verbose_name="联系方式", max_length=11)
    user_logo = models.CharField(verbose_name="用户图像", max_length=64, null=True, blank=True)
    company_id = models.IntegerField(verbose_name="企业id")
    company_name = models.CharField(verbose_name="企业名字", max_length=320)
    role_id = models.IntegerField(verbose_name="角色ID")
    role_name = models.CharField(verbose_name="角色名", max_length=32)
    service_start_date = models.DateTimeField(verbose_name="服务开始时间")
    service_end_date = models.DateTimeField(verbose_name="服务结束时间")
    user_state = models.CharField(verbose_name="用户状态", choices=UserState, max_length=1)
    isdel = models.CharField(verbose_name="删除标记", choices=IsDel, max_length=1)
    createtime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __unicode__(self):
        return self.user_name

    class Meta:
        db_table = 'sem_user_info'
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'


class Company(models.Model):

    State = (
        ("0", '停用'),
        ("1", '启用'),
    )
    IsDel = (
        ("0", '否'),
        ("1", '是'),
    )

    company_id = models.AutoField(verbose_name="企业ID", primary_key=True)
    company_name = models.CharField(verbose_name="企业名字", max_length=320)
    company_simple_name = models.CharField(verbose_name="企业简称", max_length=320)
    company_web = models.CharField(verbose_name="企业官网地址", max_length=320, null=True, blank=True)
    company_weibo = models.CharField(verbose_name="企业微博", max_length=320, null=True, blank=True)
    company_weixin = models.CharField(verbose_name="企业微信", max_length=320, null=True, blank=True)
    company_tieba = models.CharField(verbose_name="企业贴吧", max_length=320, null=True, blank=True)
    company_zhidao = models.CharField(verbose_name="企业知道", max_length=320, null=True, blank=True)
    monitor_range = models.CharField(verbose_name="监控范围(1:搜索引擎,2:微博,3:微信,4:知乎,"
                                     "5:百度知道,6:百度贴吧,7:官网搜索,8:应用商店)", max_length=32)
    monitor_state = models.CharField(verbose_name="监控状态", choices=State, max_length=1)
    service_start_date = models.DateTimeField(verbose_name="服务开始时间")
    service_end_date = models.DateTimeField(verbose_name="服务结束时间")
    isdel = models.CharField(verbose_name="删除标记", choices=IsDel, max_length=1)
    createtime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __unicode__(self):
        return self.company_name

    class Meta:
        db_table = 'monitor_company_info'
        verbose_name = '企业信息'
        verbose_name_plural = '企业信息'


class Product(models.Model):

    IsDel = (
        ("0", '否'),
        ("1", '是'),
    )

    product_id = models.AutoField(verbose_name="产品ID", primary_key=True)
    company_id = models.IntegerField(verbose_name="企业ID")
    company_name = models.CharField(verbose_name="企业名字", max_length=320)
    product_name = models.CharField(verbose_name="产品名称", max_length=320)
    product_simple_name = models.CharField(verbose_name="产品简称", max_length=320)
    product_web = models.CharField(verbose_name="产品官网", max_length=320, null=True, blank=True)
    product_weibo = models.CharField(verbose_name="产品微博", max_length=320, null=True, blank=True)
    product_weixin = models.CharField(verbose_name="产品微信", max_length=320, null=True, blank=True)
    product_tieba = models.CharField(verbose_name="产品贴吧", max_length=320, null=True, blank=True)
    product_keyword = models.CharField(verbose_name="产品关键字", max_length=320)
    monitor_range = models.CharField(verbose_name="监控范围", max_length=32)
    isdel = models.CharField(verbose_name="删除标记", choices=IsDel, max_length=1)
    createtime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __unicode__(self):
        return self.product_name

    class Meta:
        db_table = 'monitor_product_info'
        verbose_name = '产品信息'
        verbose_name_plural = '产品信息'


class App(models.Model):

    IsDel = (
        ("0", '否'),
        ("1", '是'),
    )

    app_id = models.AutoField(verbose_name="应用程序ID", primary_key=True)
    company_id = models.IntegerField(verbose_name="企业ID")
    company_name = models.CharField(verbose_name="企业名字", max_length=320)
    product_id = models.IntegerField(verbose_name="关联产品ID")
    product_name = models.CharField(verbose_name="关联产品名称", max_length=320)
    appstore_id = models.CharField(verbose_name="应用程序在appstore的ID", max_length=32)
    app_name = models.CharField(verbose_name="应用程序名字", max_length=32)
    isdel = models.CharField(verbose_name="删除标记", choices=IsDel, max_length=1)
    createtime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __unicode__(self):
        return self.app_name

    class Meta:
        db_table = 'monitor_app_info'
        verbose_name = '应用程序信息'
        verbose_name_plural = '应用程序信息'


class Event(models.Model):

    State = (
        ("0", '停用'),
        ("1", '启用'),
    )
    IsDel = (
        ("0", '否'),
        ("1", '是'),
    )

    event_id = models.AutoField(verbose_name="事件ID", primary_key=True)
    company_id = models.IntegerField(verbose_name="企业ID")
    company_name = models.CharField(verbose_name="企业名字", max_length=320)
    event_name = models.CharField(verbose_name="事件名", max_length=320)
    event_keyword = models.CharField(verbose_name="事件关键词", max_length=320)
    event_ambiguous_word = models.CharField(verbose_name="事件歧义词", max_length=320)
    monitor_range = models.CharField(verbose_name="监控范围", max_length=32)
    service_start_date = models.DateTimeField(verbose_name="服务开始时间")
    service_end_date = models.DateTimeField(verbose_name="服务结束时间")
    monitor_state = models.CharField(verbose_name="监控状态", choices=State, max_length=1)
    isdel = models.CharField(verbose_name="删除标记", choices=IsDel, max_length=1)
    createtime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __unicode__(self):
        return self.event_name

    class Meta:
        db_table = 'monitor_event_info'
        verbose_name = '事件信息'
        verbose_name_plural = '事件信息'


class CompeteCompany(models.Model):

    State = (
        ("0", '停用'),
        ("1", '启用'),
    )
    IsDel = (
        ("0", '否'),
        ("1", '是'),
    )

    compete_company_id = models.AutoField(verbose_name="竞品企业ID", primary_key=True)
    company_id = models.IntegerField(verbose_name="企业ID")
    company_name = models.CharField(verbose_name="企业名字", max_length=320)
    compete_company_name = models.CharField(verbose_name="竞品企业名字", max_length=320)
    compete_company_simple_name = models.CharField(verbose_name="竞品企业简称", max_length=320)
    compete_company_web = models.CharField(verbose_name="竞品企业官网地址", max_length=320, null=True, blank=True)
    compete_company_weibo = models.CharField(verbose_name="竞品企业微博", max_length=320, null=True, blank=True)
    compete_company_weixin = models.CharField(verbose_name="竞品企业微信", max_length=320, null=True, blank=True)
    compete_company_tieba = models.CharField(verbose_name="竞品企业贴吧", max_length=320, null=True, blank=True)
    compete_company_zhidao = models.CharField(verbose_name="竞品企业知道", max_length=320, null=True, blank=True)
    monitor_range = models.CharField(verbose_name="监控范围(1:搜索引擎,2:微博,3:微信,4:知乎,"
                                     "5:百度知道,6:百度贴吧,7:官网搜索,8:应用商店)", max_length=32)
    service_start_date = models.DateTimeField(verbose_name="服务开始时间")
    service_end_date = models.DateTimeField(verbose_name="服务结束时间")
    monitor_state = models.CharField(verbose_name="监控状态", choices=State, max_length=1)
    isdel = models.CharField(verbose_name="删除标记", choices=IsDel, max_length=1)
    createtime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __unicode__(self):
        return self.compete_company_name

    class Meta:
        db_table = 'monitor_compete_company_info'
        verbose_name = '竞品企业信息'
        verbose_name_plural = '竞品企业信息'


class CompeteProduct(models.Model):

    IsDel = (
        ("0", '否'),
        ("1", '是'),
    )

    compete_product_id = models.AutoField(verbose_name="竞品产品ID", primary_key=True)
    company_id = models.IntegerField(verbose_name="企业ID")
    company_name = models.CharField(verbose_name="企业名字", max_length=320)
    refer_product_id = models.IntegerField(verbose_name="竞品参照产品id")
    refer_product_name = models.CharField(verbose_name="竞品参照产品名", max_length=320)
    compete_product_name = models.CharField(verbose_name="竞品产品名称", max_length=320)
    compete_product_simple_name = models.CharField(verbose_name="竞品产品简称", max_length=320)
    compete_product_web = models.CharField(verbose_name="竞品产品官网", max_length=320, null=True, blank=True)
    compete_product_weibo = models.CharField(verbose_name="竞品产品微博", max_length=320, null=True, blank=True)
    compete_product_weixin = models.CharField(verbose_name="竞品产品微信", max_length=320, null=True, blank=True)
    compete_product_tieba = models.CharField(verbose_name="竞品产品贴吧", max_length=320, null=True, blank=True)
    compete_product_zhidao = models.CharField(verbose_name="竞品产品知道", max_length=320, null=True, blank=True)
    compete_product_keyword = models.CharField(verbose_name="竞品产品关键字", max_length=320)
    monitor_range = models.CharField(verbose_name="监控范围", max_length=32)
    isdel = models.CharField(verbose_name="删除标记", choices=IsDel, max_length=1)
    createtime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __unicode__(self):
        return self.compete_product_name

    class Meta:
        db_table = 'monitor_compete_product_info'
        verbose_name = '竞品产品信息'
        verbose_name_plural = '竞品产品信息'


class CompeteApp(models.Model):

    IsDel = (
        ("0", '否'),
        ("1", '是'),
    )

    compete_app_id = models.AutoField(verbose_name="竞品应用程序ID", primary_key=True)
    company_id = models.IntegerField(verbose_name="企业ID")
    company_name = models.CharField(verbose_name="企业名字", max_length=320)
    refer_appstore_id = models.CharField(verbose_name="竞品APP参照APP_ID", max_length=32)
    refer_app_name = models.CharField(verbose_name="竞品APP参考APP名字", max_length=32)
    compete_appstore_id = models.CharField(verbose_name="竞品应用程序在appstore的ID", max_length=32)
    compete_app_name = models.CharField(verbose_name="竞品应用程序名字", max_length=32)
    isdel = models.CharField(verbose_name="删除标记", choices=IsDel, max_length=1)
    createtime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __unicode__(self):
        return self.compete_app_name

    class Meta:
        db_table = 'monitor_compete_app_info'
        verbose_name = '竞品应用程序信息'
        verbose_name_plural = '竞品应用程序信息'


class CompanyInfluenceInfo(models.Model):

    IsDel = (
        ("0", '否'),
        ("1", '是'),
    )

    influence_id = models.AutoField(verbose_name="主键ID", primary_key=True)
    company_id = models.IntegerField(verbose_name="企业ID")
    company_name = models.CharField(verbose_name="企业名字", max_length=320)
    official_news_count = models.IntegerField(verbose_name="官方新闻数")
    official_wb_article_count = models.IntegerField(verbose_name="官方微博文章数")
    official_wb_comment_count = models.IntegerField(verbose_name="官方微博文章评论数")
    official_wb_likes_count = models.IntegerField(verbose_name="官方微博文章点赞数")
    official_wb_repost_count = models.IntegerField(verbose_name="官方微博文章转发数")
    official_wx_article_count = models.IntegerField(verbose_name="官方微信文章数")
    official_wx_article_view_count = models.IntegerField(verbose_name="官方微信文章阅读数")
    official_app_score = models.IntegerField(verbose_name="官方应用评分")
    official_article_count = models.IntegerField(verbose_name="官网文章数")
    tieba_article_count = models.IntegerField(verbose_name="贴吧文章数")
    tieba_article_reply_count = models.IntegerField(verbose_name="贴吧文章回复数")
    se_search_article_count = models.IntegerField(verbose_name="搜索引擎搜索文章数")
    wb_search_article_count = models.IntegerField(verbose_name="微信搜索文章数")
    wx_search_article_count = models.IntegerField(verbose_name="知道搜索问题数")
    zd_search_question_count = models.IntegerField(verbose_name="知道搜索问题数")
    zd_search_reply_count = models.IntegerField(verbose_name="知道搜索问题回复数")
    zh_search_article_count = models.IntegerField(verbose_name="知乎搜索文章数")
    zh_search_reply_count = models.IntegerField(verbose_name="知乎搜索文章回复数")
    isdel = models.CharField(verbose_name="删除标记", choices=IsDel, max_length=1)
    createtime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __unicode__(self):
        return self.company_name

    class Meta:
        db_table = 'company_influence_info'
        verbose_name = '企业影响力信息表'
        verbose_name_plural = '企业影响力信息表'


class SemMonitorCrawlInfo(models.Model):
    IsDel = (
        ("0", '否'),
        ("1", '是'),
    )

    State = (
        ("0", '停用'),
        ("1", '启用'),
    )

    MonitorType = (
        ("1", "企业监控"),
        ("2", "产品监控"),
        ("3", "app监控"),
        ("4", "事件监控"),
        ("5", "竞品企业监控"),
        ("6", "竞品产品监控"),
        ("7", "竞品app监控"),
    )

    DataSourceType = (
        ('1', "名称"),
        ('2', "简称"),
        ('3', "官网"),
        ('4', "微博"),
        ('5', "微信"),
        ('6', "知乎"),
        ('7', "知道"),
        ('8', "贴吧"),
    )

    id = models.AutoField(primary_key=True)
    company_id = models.IntegerField(verbose_name="企业ID")
    company_name = models.CharField(verbose_name="企业名字", max_length=320)
    monitor_type_id = models.CharField(verbose_name="监控范围", choices=MonitorType, max_length=1)
    data_source_type = models.CharField(verbose_name="爬虫任务源类型", choices=DataSourceType, max_length=1)
    data_source_id = models.CharField(verbose_name="爬虫任务源ID", max_length=32)
    monitor_id = models.IntegerField(verbose_name="监控计划ID")
    monitor_range = models.CharField(verbose_name="监控范围(1:搜索引擎,2:微博,3:微信,4:知乎,"
                                     "5:百度知道,6:百度贴吧,7:官网搜索,8:应用商店)", max_length=32)

    monitor_state = models.CharField(verbose_name="监控状态", choices=State, max_length=1)
    isdel = models.CharField(verbose_name="删除标记", choices=IsDel, max_length=1)
    createtime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __unicode__(self):
        return self.company_name

    class Meta:
        db_table = 'sem_monitor_crawl_info'
        verbose_name = '监控计划与爬虫任务关系表'
        verbose_name_plural = '监控计划与爬虫任务关系表'
