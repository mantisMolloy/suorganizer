# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(help_text='A label for URL config.', max_length=31, unique=True)),
                ('text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='date published')),
                ('startup', models.ManyToManyField(related_name='blog_post', to='organizer.Startup')),
                ('tags', models.ManyToManyField(related_name='blog_post', to='organizer.Tag')),
            ],
        ),
    ]
