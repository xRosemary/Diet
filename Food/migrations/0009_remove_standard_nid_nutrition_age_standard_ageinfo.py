# Generated by Django 4.0.1 on 2022-05-04 04:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0008_remove_nutrition_eer_remove_nutrition_va_and_more'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='standard',
        #     name='nid',
        # ),
        # migrations.AddField(
        #     model_name='nutrition',
        #     name='age',
        #     field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='年龄'),
        # ),
        # migrations.AddField(
        #     model_name='standard',
        #     name='ageInfo',
        #     field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Food.nutrition', verbose_name='年龄'),
        #     preserve_default=False,
        # ),
    ]
