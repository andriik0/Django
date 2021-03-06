# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-04-11 07:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forgot_lessons_search', '0003_auto_20210411_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationslog',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='log', to='timeline.Entry'),
        ),
        migrations.AlterField(
            model_name='notificationslog',
            name='subscription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='log', to='market.Subscription'),
        ),
    ]
