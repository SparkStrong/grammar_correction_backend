# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackResult',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('user_name', models.CharField(max_length=64)),
                ('original_text', models.TextField(blank=True, null=True)),
                ('system_correction_result', models.TextField(blank=True, null=True)),
                ('user_correction_suggestion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('user_name', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=128)),
                ('user_type', models.IntegerField()),
            ],
        ),
    ]
