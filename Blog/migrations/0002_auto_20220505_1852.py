# Generated by Django 3.2 on 2022-05-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': '文章信息'},
        ),
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='发布日期'),
        ),
    ]
