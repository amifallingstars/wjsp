# Generated by Django 3.2.4 on 2021-06-16 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0014_auto_20210617_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodstags',
            old_name='imgSrc',
            new_name='tags',
        ),
    ]
