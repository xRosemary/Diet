# Generated by Django 4.0.1 on 2022-05-02 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserInfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthrecord',
            name='illness',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserInfo.illnessmode', verbose_name='疾病名称'),
        ),
    ]
