# Generated by Django 3.2.4 on 2021-06-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0002_auto_20210605_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_info',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='users',
            name='phoneNum',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='users',
            name='qq',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
