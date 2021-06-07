# Generated by Django 3.2.4 on 2021-06-07 01:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('simc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battlefield',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='battlefield',
            name='delete_flag',
            field=models.SmallIntegerField(default=0, verbose_name='删除标记'),
        ),
        migrations.AlterField(
            model_name='battlefield',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='card',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='card',
            name='delete_flag',
            field=models.SmallIntegerField(default=0, verbose_name='删除标记'),
        ),
        migrations.AlterField(
            model_name='card',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='character',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='character',
            name='delete_flag',
            field=models.SmallIntegerField(default=0, verbose_name='删除标记'),
        ),
        migrations.AlterField(
            model_name='character',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='delete_flag',
            field=models.SmallIntegerField(default=0, verbose_name='删除标记'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
    ]
