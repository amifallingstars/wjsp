# Generated by Django 3.2.4 on 2021-06-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0018_alter_goodshisdata_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodshisdata',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='竞拍时间'),
        ),
    ]
