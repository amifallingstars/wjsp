# Generated by Django 3.2.4 on 2021-06-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='phoneNum',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='qq',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
