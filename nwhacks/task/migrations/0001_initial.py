# Generated by Django 2.1.5 on 2019-01-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100)),
                ('deadline', models.DateField()),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]