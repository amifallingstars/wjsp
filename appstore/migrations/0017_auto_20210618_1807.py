# Generated by Django 3.2.4 on 2021-06-18 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0016_alter_goodstags_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsimg',
            options={'verbose_name': '商品照片', 'verbose_name_plural': '商品照片'},
        ),
        migrations.AlterModelOptions(
            name='goodstags',
            options={'verbose_name': '商品标签', 'verbose_name_plural': '商品标签'},
        ),
        migrations.CreateModel(
            name='GoodsHisData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(default='', max_length=20, verbose_name='竞价')),
                ('time', models.DateTimeField(blank=True, verbose_name='竞拍时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstore.goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstore.users')),
            ],
            options={
                'verbose_name': '历史竞价',
                'verbose_name_plural': '历史竞价',
            },
        ),
    ]
