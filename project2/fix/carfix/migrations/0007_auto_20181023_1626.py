# Generated by Django 2.0.2 on 2018-10-23 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carfix', '0006_auto_20181023_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixlist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='fixlist',
            name='worker',
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_car',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='FixList',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]