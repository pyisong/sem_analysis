# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sem_index', '0003_auto_20171018_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competeproduct',
            name='compete_product_simple_name',
            field=models.CharField(max_length=320, verbose_name=b'\xe7\xab\x9e\xe5\x93\x81\xe4\xba\xa7\xe5\x93\x81\xe7\xae\x80\xe7\xa7\xb0'),
        ),
    ]
