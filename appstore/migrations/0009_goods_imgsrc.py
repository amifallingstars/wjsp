# Generated by Django 3.2.4 on 2021-06-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0008_users_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='imgSrc',
            field=models.CharField(default='http://127.0.0.1:8000/static/goods/0001.jfif', max_length=100, verbose_name='商品照片'),
        ),
    ]