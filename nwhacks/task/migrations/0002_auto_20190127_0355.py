# Generated by Django 2.1.5 on 2019-01-27 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0002_auto_20190127_0355'),
        ('user', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='goal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='goal.Goal'),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
