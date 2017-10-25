# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUserInfo',
            fields=[
                ('user_id', models.AutoField(serialize=False, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7ID', primary_key=True)),
                ('user_name', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=64, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('true_name', models.CharField(max_length=32, verbose_name=b'\xe7\x9c\x9f\xe5\xae\x9e\xe5\xa7\x93\xe5\x90\x8d')),
                ('email', models.CharField(max_length=32, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('mobile', models.CharField(max_length=11, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe6\x96\xb9\xe5\xbc\x8f')),
                ('user_logo', models.CharField(max_length=64, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x9b\xbe\xe5\x83\x8f')),
                ('company_id', models.IntegerField(verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9aid')),
                ('company_name', models.CharField(max_length=320, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d\xe5\xad\x97')),
                ('role_id', models.IntegerField(verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2ID')),
                ('role_name', models.CharField(max_length=32, verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2\xe5\x90\x8d')),
                ('service_start_date', models.DateTimeField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('service_end_date', models.DateTimeField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('user_state', models.CharField(max_length=1, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'0', b'\xe5\x81\x9c\xe7\x94\xa8'), (b'1', b'\xe5\x90\xaf\xe7\x94\xa8')])),
                ('isdel', models.CharField(max_length=1, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0', choices=[(b'0', b'\xe5\x90\xa6'), (b'1', b'\xe6\x98\xaf')])),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'sem_user_info',
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('app_id', models.AutoField(serialize=False, verbose_name=b'\xe5\xba\x94\xe7\x94\xa8\xe7\xa8\x8b\xe5\xba\x8fID', primary_key=True)),
                ('company_id', models.IntegerField(verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9aID')),
                ('company_name', models.CharField(max_length=320, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d\xe5\xad\x97')),
                ('product_id', models.IntegerField(verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe4\xba\xa7\xe5\x93\x81ID')),
                ('product_name', models.CharField(max_length=320, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('appstore_id', models.CharField(max_length=32, verbose_name=b'\xe5\xba\x94\xe7\x94\xa8\xe7\xa8\x8b\xe5\xba\x8f\xe5\x9c\xa8appstore\xe7\x9a\x84ID')),
                ('app_name', models.CharField(max_length=32, verbose_name=b'\xe5\xba\x94\xe7\x94\xa8\xe7\xa8\x8b\xe5\xba\x8f\xe5\x90\x8d\xe5\xad\x97')),
                ('isdel', models.CharField(max_length=1, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0', choices=[(b'0', b'\xe5\x90\xa6'), (b'1', b'\xe6\x98\xaf')])),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'monitor_app_info',
                'verbose_name': '\u5e94\u7528\u7a0b\u5e8f\u4fe1\u606f',
                'verbose_name_plural': '\u5e94\u7528\u7a0b\u5e8f\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(serialize=False, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9aID', primary_key=True)),
                ('company_name', models.CharField(max_length=320, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d\xe5\xad\x97')),
                ('company_simple_name', models.CharField(max_length=320, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe7\xae\x80\xe7\xa7\xb0')),
                ('company_web', models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\xae\x98\xe7\xbd\x91\xe5\x9c\xb0\xe5\x9d\x80')),
                ('company_weibo', models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\xbe\xae\xe5\x8d\x9a')),
                ('company_weixin', models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\xbe\xae\xe4\xbf\xa1')),
                ('company_tieba', models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe8\xb4\xb4\xe5\x90\xa7')),
                ('company_zhidao', models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe7\x9f\xa5\xe9\x81\x93')),
                ('monitor_range', models.CharField(max_length=32, verbose_name=b'\xe7\x9b\x91\xe6\x8e\xa7\xe8\x8c\x83\xe5\x9b\xb4(1:\xe6\x90\x9c\xe7\xb4\xa2\xe5\xbc\x95\xe6\x93\x8e,2:\xe5\xbe\xae\xe5\x8d\x9a,3:\xe5\xbe\xae\xe4\xbf\xa1,4:\xe7\x9f\xa5\xe4\xb9\x8e,5:\xe7\x99\xbe\xe5\xba\xa6\xe7\x9f\xa5\xe9\x81\x93,6:\xe7\x99\xbe\xe5\xba\xa6\xe8\xb4\xb4\xe5\x90\xa7,7:\xe5\xae\x98\xe7\xbd\x91\xe6\x90\x9c\xe7\xb4\xa2,8:\xe5\xba\x94\xe7\x94\xa8\xe5\x95\x86\xe5\xba\x97)')),
                ('monitor_state', models.CharField(max_length=1, verbose_name=b'\xe7\x9b\x91\xe6\x8e\xa7\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'0', b'\xe5\x81\x9c\xe7\x94\xa8'), (b'1', b'\xe5\x90\xaf\xe7\x94\xa8')])),
                ('service_start_date', models.DateTimeField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('service_end_date', models.DateTimeField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('isdel', models.CharField(max_length=1, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0', choices=[(b'0', b'\xe5\x90\xa6'), (b'1', b'\xe6\x98\xaf')])),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'monitor_company_info',
                'verbose_name': '\u4f01\u4e1a\u4fe1\u606f',
                'verbose_name_plural': '\u4f01\u4e1a\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='CompanyInfluenceInfo',
            fields=[
                ('influence_id', models.AutoField(serialize=False, verbose_name=b'\xe4\xb8\xbb\xe9\x94\xaeID', primary_key=True)),
                ('company_id', models.IntegerField(verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9aID')),
                ('company_name', models.CharField(max_length=320, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d\xe5\xad\x97')),
                ('official_news_count', models.IntegerField(verbose_name=b'\xe5\xae\x98\xe6\x96\xb9\xe6\x96\xb0\xe9\x97\xbb\xe6\x95\xb0')),
                ('official_wb_article_count', models.IntegerField(verbose_name=b'\xe5\xae\x98\xe6\x96\xb9\xe5\xbe\xae\xe5\x8d\x9a\xe6\x96\x87\xe7\xab\xa0\xe6\x95\xb0')),
                ('official_wb_comment_count', models.IntegerField(verbose_name=b'\xe5\xae\x98\xe6\x96\xb9\xe5\xbe\xae\xe5\x8d\x9a\xe6\x96\x87\xe7\xab\xa0\xe8\xaf\x84\xe8\xae\xba\xe6\x95\xb0')),
                ('official_wb_likes_count', models.IntegerField(verbose_name=b'\xe5\xae\x98\xe6\x96\xb9\xe5\xbe\xae\xe5\x8d\x9a\xe6\x96\x87\xe7\xab\xa0\xe7\x82\xb9\xe8\xb5\x9e\xe6\x95\xb0')),
                ('official_wb_repost_count', models.IntegerField(verbose_name=b'\xe5\xae\x98\xe6\x96\xb9\xe5\xbe\xae\xe5\x8d\x9a\xe6\x96\x87\xe7\xab\xa0\xe8\xbd\xac\xe5\x8f\x91\xe6\x95\xb0')),
                ('official_wx_article_count', models.IntegerField(verbose_name=b'\xe5\xae\x98\xe6\x96\xb9\xe5\xbe\xae\xe4\xbf\xa1\xe6\x96\x87\xe7\xab\xa0\xe6\x95\xb0')),
                ('official_wx_article_view_count', models.IntegerField(verbose_name=b'\xe5\xae\x98\xe6\x96\xb9\xe5\xbe\xae\xe4\xbf\xa1\xe6\x96\x87\xe7\xab\xa0\xe9\x98\x85\xe8\xaf\xbb\xe6\x95\xb0')),
                ('official_app_score', models.IntegerField(verbose_name=b'\xe5\xae\x98\xe6\x96\xb9\xe5\xba\x94\xe7\x94\xa8\xe8\xaf\x84\xe5\x88\x86')),
                ('official_article_count', models.IntegerField(verbose_name=b'\xe5\xae\x98\xe7\xbd\x91\xe6\x96\x87\xe7\xab\xa0\xe6\x95\xb0')),
                ('tieba_article_count', models.IntegerField(verbose_name=b'\xe8\xb4\xb4\xe5\x90\xa7\xe6\x96\x87\xe7\xab\xa0\xe6\x95\xb0')),
                ('tieba_article_reply_count', models.IntegerField(verbose_name=b'\xe8\xb4\xb4\xe5\x90\xa7\xe6\x96\x87\xe7\xab\xa0\xe5\x9b\x9e\xe5\xa4\x8d\xe6\x95\xb0')),
                ('se_search_article_count', models.IntegerField(verbose_name=b'\xe6\x90\x9c\xe7\xb4\xa2\xe5\xbc\x95\xe6\x93\x8e\xe6\x90\x9c\xe7\xb4\xa2\xe6\x96\x87\xe7\xab\xa0\xe6\x95\xb0')),
                ('wb_search_article_count', models.IntegerField(verbose_name=b'\xe5\xbe\xae\xe4\xbf\xa1\xe6\x90\x9c\xe7\xb4\xa2\xe6\x96\x87\xe7\xab\xa0\xe6\x95\xb0')),
                ('wx_search_article_count', models.IntegerField(verbose_name=b'\xe7\x9f\xa5\xe9\x81\x93\xe6\x90\x9c\xe7\xb4\xa2\xe9\x97\xae\xe9\xa2\x98\xe6\x95\xb0')),
                ('zd_search_question_count', models.IntegerField(verbose_name=b'\xe7\x9f\xa5\xe9\x81\x93\xe6\x90\x9c\xe7\xb4\xa2\xe9\x97\xae\xe9\xa2\x98\xe6\x95\xb0')),
                ('zd_search_reply_count', models.IntegerField(verbose_name=b'\xe7\x9f\xa5\xe9\x81\x93\xe6\x90\x9c\xe7\xb4\xa2\xe9\x97\xae\xe9\xa2\x98\xe5\x9b\x9e\xe5\xa4\x8d\xe6\x95\xb0')),
                ('zh_search_article_count', models.IntegerField(verbose_name=b'\xe7\x9f\xa5\xe4\xb9\x8e\xe6\x90\x9c\xe7\xb4\xa2\xe6\x96\x87\xe7\xab\xa0\xe6\x95\xb0')),
                ('zh_search_reply_count', models.IntegerField(verbose_name=b'\xe7\x9f\xa5\xe4\xb9\x8e\xe6\x90\x9c\xe7\xb4\xa2\xe6\x96\x87\xe7\xab\xa0\xe5\x9b\x9e\xe5\xa4\x8d\xe6\x95\xb0')),
                ('isdel', models.CharField(max_length=1, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0', choices=[(b'0', b'\xe5\x90\xa6'), (b'1', b'\xe6\x98\xaf')])),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'company_influence_info',
                'verbose_name': '\u4f01\u4e1a\u5f71\u54cd\u529b\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u4f01\u4e1a\u5f71\u54cd\u529b\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='CompeteApp',
            fields=[
                ('compete_app_id', models.AutoField(serialize=False, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe5\xba\x94\xe7\x94\xa8\xe7\xa8\x8b\xe5\xba\x8fID', primary_key=True)),
                ('company_id', models.IntegerField(verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9aID')),
                ('company_name', models.CharField(max_length=320, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d\xe5\xad\x97')),
                ('refer_appstore_id', models.CharField(max_length=32, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81APP\xe5\x8f\x82\xe7\x85\xa7APP_ID')),
                ('refer_app_name', models.CharField(max_length=32, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81APP\xe5\x8f\x82\xe8\x80\x83APP\xe5\x90\x8d\xe5\xad\x97')),
                ('compete_appstore_id', models.CharField(max_length=32, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe5\xba\x94\xe7\x94\xa8\xe7\xa8\x8b\xe5\xba\x8f\xe5\x9c\xa8appstore\xe7\x9a\x84ID')),
                ('compete_app_name', models.CharField(max_length=32, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe5\xba\x94\xe7\x94\xa8\xe7\xa8\x8b\xe5\xba\x8f\xe5\x90\x8d\xe5\xad\x97')),
                ('isdel', models.CharField(max_length=1, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0', choices=[(b'0', b'\xe5\x90\xa6'), (b'1', b'\xe6\x98\xaf')])),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'monitor_compete_app_info',
                'verbose_name': '\u7ade\u54c1\u5e94\u7528\u7a0b\u5e8f\u4fe1\u606f',
                'verbose_name_plural': '\u7ade\u54c1\u5e94\u7528\u7a0b\u5e8f\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='CompeteCompany',
            fields=[
                ('compete_company_id', models.AutoField(serialize=False, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9aID', primary_key=True)),
                ('company_id', models.IntegerField(verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9aID')),
                ('company_name', models.CharField(max_length=320, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d\xe5\xad\x97')),
                ('compete_company_name', models.CharField(max_length=320, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d\xe5\xad\x97')),
                ('compete_company_simple_name', models.CharField(max_length=320, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9a\xe7\xae\x80\xe7\xa7\xb0')),
                ('compete_company_web', models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9a\xe5\xae\x98\xe7\xbd\x91\xe5\x9c\xb0\xe5\x9d\x80')),
                ('compete_company_weibo', models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9a\xe5\xbe\xae\xe5\x8d\x9a')),
                ('compete_company_weixin', models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9a\xe5\xbe\xae\xe4\xbf\xa1')),
                ('compete_company_tieba', models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9a\xe8\xb4\xb4\xe5\x90\xa7')),
                ('compete_company_zhidao', models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9a\xe7\x9f\xa5\xe9\x81\x93')),
                ('monitor_range', models.CharField(max_length=32, verbose_name=b'\xe7\x9b\x91\xe6\x8e\xa7\xe8\x8c\x83\xe5\x9b\xb4(1:\xe6\x90\x9c\xe7\xb4\xa2\xe5\xbc\x95\xe6\x93\x8e,2:\xe5\xbe\xae\xe5\x8d\x9a,3:\xe5\xbe\xae\xe4\xbf\xa1,4:\xe7\x9f\xa5\xe4\xb9\x8e,5:\xe7\x99\xbe\xe5\xba\xa6\xe7\x9f\xa5\xe9\x81\x93,6:\xe7\x99\xbe\xe5\xba\xa6\xe8\xb4\xb4\xe5\x90\xa7,7:\xe5\xae\x98\xe7\xbd\x91\xe6\x90\x9c\xe7\xb4\xa2,8:\xe5\xba\x94\xe7\x94\xa8\xe5\x95\x86\xe5\xba\x97)')),
                ('service_start_date', models.DateTimeField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('service_end_date', models.DateTimeField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('monitor_state', models.CharField(max_length=1, verbose_name=b'\xe7\x9b\x91\xe6\x8e\xa7\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'0', b'\xe5\x81\x9c\xe7\x94\xa8'), (b'1', b'\xe5\x90\xaf\xe7\x94\xa8')])),
                ('isdel', models.CharField(max_length=1, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0', choices=[(b'0', b'\xe5\x90\xa6'), (b'1', b'\xe6\x98\xaf')])),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'monitor_compete_company_info',
                'verbose_name': '\u7ade\u54c1\u4f01\u4e1a\u4fe1\u606f',
                'verbose_name_plural': '\u7ade\u54c1\u4f01\u4e1a\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='CompeteProduct',
            fields=[
                ('compete_product_id', models.AutoField(serialize=False, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81ID', primary_key=True)),
                ('company_id', models.IntegerField(verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9aID')),
                ('company_name', models.CharField(max_length=320, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d\xe5\xad\x97')),
                ('refer_product_id', models.IntegerField(verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe5\x8f\x82\xe7\x85\xa7\xe4\xba\xa7\xe5\x93\x81id')),
                ('refer_product_name', models.CharField(max_length=320, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe5\x8f\x82\xe7\x85\xa7\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d')),
                ('compete_product_name', models.CharField(max_length=320, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('compete_product_simple_name', models.CharField(max_length=320, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('compete_product_web', models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe5\xae\x98\xe7\xbd\x91')),
                ('compete_product_weibo', models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe5\xbe\xae\xe5\x8d\x9a')),
                ('compete_product_weixin', models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe5\xbe\xae\xe4\xbf\xa1')),
                ('compete_product_tieba', models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe8\xb4\xb4\xe5\x90\xa7')),
                ('compete_product_zhidao', models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe7\x9f\xa5\xe9\x81\x93')),
                ('compete_product_keyword', models.CharField(max_length=320, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97')),
                ('monitor_range', models.CharField(max_length=32, verbose_name=b'\xe7\x9b\x91\xe6\x8e\xa7\xe8\x8c\x83\xe5\x9b\xb4')),
                ('isdel', models.CharField(max_length=1, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0', choices=[(b'0', b'\xe5\x90\xa6'), (b'1', b'\xe6\x98\xaf')])),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'monitor_compete_product_info',
                'verbose_name': '\u7ade\u54c1\u4ea7\u54c1\u4fe1\u606f',
                'verbose_name_plural': '\u7ade\u54c1\u4ea7\u54c1\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(serialize=False, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6ID', primary_key=True)),
                ('company_id', models.IntegerField(verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9aID')),
                ('company_name', models.CharField(max_length=320, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d\xe5\xad\x97')),
                ('event_name', models.CharField(max_length=320, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe5\x90\x8d')),
                ('event_keyword', models.CharField(max_length=320, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe5\x85\xb3\xe9\x94\xae\xe8\xaf\x8d')),
                ('event_ambiguous_word', models.CharField(max_length=320, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe6\xad\xa7\xe4\xb9\x89\xe8\xaf\x8d')),
                ('monitor_range', models.CharField(max_length=32, verbose_name=b'\xe7\x9b\x91\xe6\x8e\xa7\xe8\x8c\x83\xe5\x9b\xb4')),
                ('service_start_date', models.DateTimeField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('service_end_date', models.DateTimeField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('monitor_state', models.CharField(max_length=1, verbose_name=b'\xe7\x9b\x91\xe6\x8e\xa7\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'0', b'\xe5\x81\x9c\xe7\x94\xa8'), (b'1', b'\xe5\x90\xaf\xe7\x94\xa8')])),
                ('isdel', models.CharField(max_length=1, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0', choices=[(b'0', b'\xe5\x90\xa6'), (b'1', b'\xe6\x98\xaf')])),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'monitor_event_info',
                'verbose_name': '\u4e8b\u4ef6\u4fe1\u606f',
                'verbose_name_plural': '\u4e8b\u4ef6\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(serialize=False, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81ID', primary_key=True)),
                ('company_id', models.IntegerField(verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9aID')),
                ('company_name', models.CharField(max_length=320, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d\xe5\xad\x97')),
                ('product_name', models.CharField(max_length=320, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('product_simple_name', models.CharField(max_length=320, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xae\x80\xe7\xa7\xb0')),
                ('product_web', models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\xae\x98\xe7\xbd\x91')),
                ('product_weibo', models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\xbe\xae\xe5\x8d\x9a')),
                ('product_weixin', models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\xbe\xae\xe4\xbf\xa1')),
                ('product_tieba', models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe8\xb4\xb4\xe5\x90\xa7')),
                ('product_keyword', models.CharField(max_length=320, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97')),
                ('monitor_range', models.CharField(max_length=32, verbose_name=b'\xe7\x9b\x91\xe6\x8e\xa7\xe8\x8c\x83\xe5\x9b\xb4')),
                ('isdel', models.CharField(max_length=1, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0', choices=[(b'0', b'\xe5\x90\xa6'), (b'1', b'\xe6\x98\xaf')])),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'monitor_product_info',
                'verbose_name': '\u4ea7\u54c1\u4fe1\u606f',
                'verbose_name_plural': '\u4ea7\u54c1\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='SemMonitorCrawlInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('company_id', models.IntegerField(verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9aID')),
                ('company_name', models.CharField(max_length=320, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d\xe5\xad\x97')),
                ('monitor_type_id', models.CharField(max_length=1, verbose_name=b'\xe7\x9b\x91\xe6\x8e\xa7\xe8\x8c\x83\xe5\x9b\xb4', choices=[(b'1', b'\xe4\xbc\x81\xe4\xb8\x9a\xe7\x9b\x91\xe6\x8e\xa7'), (b'2', b'\xe4\xba\xa7\xe5\x93\x81\xe7\x9b\x91\xe6\x8e\xa7'), (b'3', b'app\xe7\x9b\x91\xe6\x8e\xa7'), (b'4', b'\xe4\xba\x8b\xe4\xbb\xb6\xe7\x9b\x91\xe6\x8e\xa7'), (b'5', b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9a\xe7\x9b\x91\xe6\x8e\xa7'), (b'6', b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe7\x9b\x91\xe6\x8e\xa7'), (b'7', b'\xe7\xab\x9e\xe5\x93\x81app\xe7\x9b\x91\xe6\x8e\xa7')])),
                ('data_source_type', models.CharField(max_length=1, verbose_name=b'\xe7\x88\xac\xe8\x99\xab\xe4\xbb\xbb\xe5\x8a\xa1\xe6\xba\x90\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'1', b'\xe5\x90\x8d\xe7\xa7\xb0'), (b'2', b'\xe7\xae\x80\xe7\xa7\xb0'), (b'3', b'\xe5\xae\x98\xe7\xbd\x91'), (b'4', b'\xe5\xbe\xae\xe5\x8d\x9a'), (b'5', b'\xe5\xbe\xae\xe4\xbf\xa1'), (b'6', b'\xe7\x9f\xa5\xe4\xb9\x8e'), (b'7', b'\xe7\x9f\xa5\xe9\x81\x93'), (b'8', b'\xe8\xb4\xb4\xe5\x90\xa7')])),
                ('data_source_id', models.CharField(max_length=32, verbose_name=b'\xe7\x88\xac\xe8\x99\xab\xe4\xbb\xbb\xe5\x8a\xa1\xe6\xba\x90ID')),
                ('monitor_id', models.IntegerField(verbose_name=b'\xe7\x9b\x91\xe6\x8e\xa7\xe8\xae\xa1\xe5\x88\x92ID')),
                ('is_compete', models.CharField(max_length=1, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe6\xa0\x87\xe8\xae\xb0', choices=[(b'0', b'\xe5\x90\xa6'), (b'1', b'\xe6\x98\xaf')])),
                ('monitor_range', models.CharField(max_length=32, verbose_name=b'\xe7\x9b\x91\xe6\x8e\xa7\xe8\x8c\x83\xe5\x9b\xb4(1:\xe6\x90\x9c\xe7\xb4\xa2\xe5\xbc\x95\xe6\x93\x8e,2:\xe5\xbe\xae\xe5\x8d\x9a,3:\xe5\xbe\xae\xe4\xbf\xa1,4:\xe7\x9f\xa5\xe4\xb9\x8e,5:\xe7\x99\xbe\xe5\xba\xa6\xe7\x9f\xa5\xe9\x81\x93,6:\xe7\x99\xbe\xe5\xba\xa6\xe8\xb4\xb4\xe5\x90\xa7,7:\xe5\xae\x98\xe7\xbd\x91\xe6\x90\x9c\xe7\xb4\xa2,8:\xe5\xba\x94\xe7\x94\xa8\xe5\x95\x86\xe5\xba\x97)')),
                ('monitor_state', models.CharField(max_length=1, verbose_name=b'\xe7\x9b\x91\xe6\x8e\xa7\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'0', b'\xe5\x81\x9c\xe7\x94\xa8'), (b'1', b'\xe5\x90\xaf\xe7\x94\xa8')])),
                ('isdel', models.CharField(max_length=1, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0', choices=[(b'0', b'\xe5\x90\xa6'), (b'1', b'\xe6\x98\xaf')])),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'sem_monitor_crawl_info',
                'verbose_name': '\u76d1\u63a7\u8ba1\u5212\u4e0e\u722c\u866b\u4efb\u52a1\u5173\u7cfb\u8868',
                'verbose_name_plural': '\u76d1\u63a7\u8ba1\u5212\u4e0e\u722c\u866b\u4efb\u52a1\u5173\u7cfb\u8868',
            },
        ),
    ]