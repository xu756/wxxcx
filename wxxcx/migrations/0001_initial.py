# Generated by Django 3.2.13 on 2022-04-23 14:19

from django.db import migrations, models
import wxxcx.methods.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
       
        migrations.CreateModel(
            name='message_img',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('message_id', models.CharField(max_length=128, verbose_name='留言id')),
                ('img', models.ImageField(storage=wxxcx.methods.storage.ImageStorage(), upload_to='message', verbose_name='留言图片')),
            ],
            options={
                'verbose_name': '留言图片',
                'verbose_name_plural': '留言图片',
            },
        )
    ]