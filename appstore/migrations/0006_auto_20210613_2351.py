# Generated by Django 3.2.4 on 2021-06-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0005_alter_usertoken_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='avatar',
            field=models.CharField(default='http://127.0.0.1:8000/static/images/uestc.png', max_length=100, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(blank=True, max_length=40, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(blank=True, max_length=10, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phoneNum',
            field=models.CharField(blank=True, max_length=11, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='users',
            name='qq',
            field=models.CharField(blank=True, max_length=40, verbose_name='QQ账号'),
        ),
    ]
