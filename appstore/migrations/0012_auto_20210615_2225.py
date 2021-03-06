# Generated by Django 3.2.4 on 2021-06-15 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0011_auto_20210615_1859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userorders',
            options={'verbose_name': '订单列表', 'verbose_name_plural': '订单列表'},
        ),
        migrations.AlterField(
            model_name='userchart',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstore.goods'),
        ),
        migrations.AlterField(
            model_name='userchart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstore.users'),
        ),
        migrations.AlterField(
            model_name='userfavorites',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstore.goods'),
        ),
        migrations.AlterField(
            model_name='userfavorites',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstore.users'),
        ),
        migrations.AlterField(
            model_name='userorders',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstore.goods'),
        ),
        migrations.AlterField(
            model_name='userorders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstore.users'),
        ),
        migrations.AlterField(
            model_name='uservip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstore.users'),
        ),
    ]
