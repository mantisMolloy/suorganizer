# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLink',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=63)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('link', models.URLField(max_length=255)),
            ],
            options={
                'get_latest_by': 'pub_date',
                'ordering': ['-pub_date'],
                'verbose_name': 'news article',
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=31, db_index=True)),
                ('slug', models.SlugField(unique=True, help_text='A label for URL config.', max_length=31)),
                ('description', models.TextField()),
                ('founded_date', models.DateField(verbose_name='date founded')),
                ('contact', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
            options={
                'get_latest_by': 'founded_date',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=31)),
                ('slug', models.SlugField(unique=True, help_text='A label for URL config.', max_length=31)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(to='organizer.Tag'),
        ),
        migrations.AddField(
            model_name='newslink',
            name='startup',
            field=models.ForeignKey(to='organizer.Startup'),
        ),
        migrations.AddField(
            model_name='newslink',
            name='tags',
            field=models.ManyToManyField(to='organizer.Tag'),
        ),
    ]
