# Generated by Django 3.2.5 on 2021-07-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PythonProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('gitlink', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='WebProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('gitlink', models.CharField(max_length=250)),
            ],
        ),
    ]
