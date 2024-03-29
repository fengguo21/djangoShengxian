# Generated by Django 2.2 on 2019-04-18 06:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsCategoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='品牌名', max_length=30, verbose_name='品牌名')),
                ('desc', models.TextField(default='', help_text='品牌描述', max_length=200, verbose_name='品牌描述')),
                ('image', models.ImageField(max_length=200, upload_to='brands/')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2019, 4, 18, 14, 46, 53, 31470), verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '宣传品牌',
                'db_table': 'goods_goodsbrand',
                'verbose_name_plural': '宣传品牌',
            },
        ),
        migrations.RemoveField(
            model_name='banner',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='category',
        ),
        migrations.RemoveField(
            model_name='goodsimage',
            name='goods',
        ),
        migrations.DeleteModel(
            name='HotSearchWords',
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 14, 46, 53, 30470), verbose_name='添加时间'),
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.DeleteModel(
            name='GoodsImage',
        ),
        migrations.AddField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
    ]
