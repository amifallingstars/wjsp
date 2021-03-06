# Generated by Django 3.2.4 on 2021-06-05 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('account', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='用户账号')),
                ('username', models.CharField(default='', max_length=40, verbose_name='用户名')),
                ('password', models.CharField(default='', max_length=16, verbose_name='用户密码')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='用户创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='用户更新时间')),
                ('isseller', models.BooleanField(default=False, verbose_name='是否为卖家')),
                ('phoneNum', models.CharField(default='', max_length=11)),
                ('qq', models.CharField(default='', max_length=40)),
                ('email', models.CharField(default='', max_length=40)),
                ('gender', models.CharField(default='', max_length=10)),
            ],
            options={
                'verbose_name': '会员账号列表',
                'verbose_name_plural': '会员账号列表',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsname', models.CharField(max_length=40, verbose_name='商品')),
                ('price', models.IntegerField(default=0, verbose_name='当前价格')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='商品创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='商品更新时间')),
                ('start_date', models.DateTimeField(default='', verbose_name='起拍时间')),
                ('end_date', models.DateTimeField(default='', verbose_name='结束拍卖时间')),
                ('goods_info', models.CharField(max_length=1000)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstore.users')),
            ],
            options={
                'verbose_name': '竞拍商品列表',
                'verbose_name_plural': '竞拍商品列表',
            },
        ),
    ]
