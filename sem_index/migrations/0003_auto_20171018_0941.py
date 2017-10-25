# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sem_index', '0002_remove_semmonitorcrawlinfo_is_compete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuserinfo',
            name='user_logo',
            field=models.CharField(max_length=64, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x9b\xbe\xe5\x83\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_tieba',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe8\xb4\xb4\xe5\x90\xa7', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_web',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\xae\x98\xe7\xbd\x91\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_weibo',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\xbe\xae\xe5\x8d\x9a', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_weixin',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\xbe\xae\xe4\xbf\xa1', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_zhidao',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe7\x9f\xa5\xe9\x81\x93', blank=True),
        ),
        migrations.AlterField(
            model_name='competecompany',
            name='compete_company_tieba',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9a\xe8\xb4\xb4\xe5\x90\xa7', blank=True),
        ),
        migrations.AlterField(
            model_name='competecompany',
            name='compete_company_web',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9a\xe5\xae\x98\xe7\xbd\x91\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
        migrations.AlterField(
            model_name='competecompany',
            name='compete_company_weibo',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9a\xe5\xbe\xae\xe5\x8d\x9a', blank=True),
        ),
        migrations.AlterField(
            model_name='competecompany',
            name='compete_company_weixin',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9a\xe5\xbe\xae\xe4\xbf\xa1', blank=True),
        ),
        migrations.AlterField(
            model_name='competecompany',
            name='compete_company_zhidao',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xbc\x81\xe4\xb8\x9a\xe7\x9f\xa5\xe9\x81\x93', blank=True),
        ),
        migrations.AlterField(
            model_name='competeproduct',
            name='compete_product_tieba',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe8\xb4\xb4\xe5\x90\xa7', blank=True),
        ),
        migrations.AlterField(
            model_name='competeproduct',
            name='compete_product_web',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe5\xae\x98\xe7\xbd\x91', blank=True),
        ),
        migrations.AlterField(
            model_name='competeproduct',
            name='compete_product_weibo',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe5\xbe\xae\xe5\x8d\x9a', blank=True),
        ),
        migrations.AlterField(
            model_name='competeproduct',
            name='compete_product_weixin',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe5\xbe\xae\xe4\xbf\xa1', blank=True),
        ),
        migrations.AlterField(
            model_name='competeproduct',
            name='compete_product_zhidao',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe7\x9f\xa5\xe9\x81\x93', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_tieba',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe8\xb4\xb4\xe5\x90\xa7', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_web',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\xae\x98\xe7\xbd\x91', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_weibo',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\xbe\xae\xe5\x8d\x9a', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_weixin',
            field=models.CharField(max_length=320, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\xbe\xae\xe4\xbf\xa1', blank=True),
        ),
    ]
