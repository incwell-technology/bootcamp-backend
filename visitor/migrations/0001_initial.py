# Generated by Django 2.1.3 on 2019-05-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('syllabus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ManyToManyField(related_name='enroll_course', to='syllabus.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=300)),
                ('middleName', models.CharField(blank=True, max_length=300, null=True)),
                ('lastName', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('gender', models.BooleanField(choices=[(True, 'Male'), (False, 'Female')], max_length=1)),
                ('education', models.CharField(max_length=800)),
                ('phone', models.CharField(max_length=500)),
                ('gitLink', models.CharField(blank=True, max_length=800, null=True)),
                ('course', models.ManyToManyField(related_name='student_course', to='syllabus.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Talk_To_Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=300)),
                ('lastName', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='enroll',
            name='student',
            field=models.ManyToManyField(related_name='enroll_student', to='visitor.Student'),
        ),
    ]
