# Generated by Django 2.2 on 2019-04-18 07:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20190418_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 15, 25, 46, 708158), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 15, 25, 46, 705158), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 15, 25, 46, 705158), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 15, 25, 46, 707159), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 15, 25, 46, 706160), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='hotsearchwords',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 15, 25, 46, 709159), verbose_name='添加时间'),
        ),
    ]
