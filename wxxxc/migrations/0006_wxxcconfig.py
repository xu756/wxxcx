# Generated by Django 3.2.13 on 2022-04-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxxxc', '0005_delete_wxxcconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='WxxcConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('key', models.CharField(max_length=50, verbose_name='配置键')),
                ('value', models.CharField(max_length=128, verbose_name='配置值')),
                ('last_update_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name': '小程序配置',
                'verbose_name_plural': '小程序配置',
            },
        ),
    ]
