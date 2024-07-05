# Generated by Django 5.0.1 on 2024-07-05 09:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.CharField(max_length=30, null=True, unique=True)),
                ('description', models.CharField(max_length=30, null=True)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='thumbnail/')),
                ('resource', models.FileField(upload_to='resource/')),
                ('course_length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('RPassword', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Learning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Prerequisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('payment_id', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.usercourse')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('serial_number', models.IntegerField()),
                ('video_id', models.FileField(upload_to='video/')),
                ('is_preview', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
        ),
    ]