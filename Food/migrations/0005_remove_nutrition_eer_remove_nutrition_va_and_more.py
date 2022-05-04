# Generated by Django 4.0.1 on 2022-05-03 15:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0004_nuttype_remove_standard_age'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='EER',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='VA',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='VB1',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='VB12',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='VB2',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='VB3',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='VB5',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='VB6',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='VB9',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='VC',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='VD',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='VE',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='VK',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='biotin',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='calcium',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='carbohydrate',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='chlorine',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='choline',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='chromium',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='copper',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='fat',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='iodine',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='iron',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='kalium',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='magnesium',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='molybdenum',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='niacinamide',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='phosphorus',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='protein',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='selenium',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='sodium',
        # ),
        # migrations.RemoveField(
        #     model_name='nutrition',
        #     name='zinc',
        # ),
        # migrations.AddField(
        #     model_name='nutrition',
        #     name='age',
        #     field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='年龄'),
        # ),
        # migrations.AddField(
        #     model_name='standard',
        #     name='TypeInfo',
        #     field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Food.nuttype', verbose_name='类别'),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='standard',
        #     name='nid',
        #     field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Food.nutrition', verbose_name='营养'),
        #     preserve_default=False,
        # ),
    ]
