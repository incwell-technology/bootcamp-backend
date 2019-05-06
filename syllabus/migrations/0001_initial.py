# Generated by Django 2.1.3 on 2019-05-06 05:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.FileField(upload_to='bootcamp/static/bootcamp/site-data/course-pictures')),
                ('description', models.TextField()),
                ('startTime', models.DateTimeField(default=datetime.datetime.now)),
                ('endTime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
                ('linkFor', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='link',
            field=models.ManyToManyField(related_name='course_links', to='syllabus.Link'),
        ),
    ]
