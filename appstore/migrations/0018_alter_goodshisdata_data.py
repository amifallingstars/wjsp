# Generated by Django 3.2.4 on 2021-06-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0017_auto_20210618_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodshisdata',
            name='data',
            field=models.IntegerField(default=0, verbose_name='竞价'),
        ),
    ]
