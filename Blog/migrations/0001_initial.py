# Generated by Django 4.0.1 on 2022-05-05 08:16

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserInfo', '0002_alter_healthrecord_illness'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='类型')),
            ],
            options={
                'verbose_name_plural': '文章类别',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='标题')),
                ('desc', models.CharField(max_length=1024, verbose_name='摘要')),
                ('content', mdeditor.fields.MDTextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserInfo.userinfo', verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.category', verbose_name='分类')),
            ],
            options={
                'verbose_name_plural': '食物信息',
            },
        ),
    ]
