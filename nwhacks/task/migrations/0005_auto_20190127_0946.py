# Generated by Django 2.1.5 on 2019-01-27 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20190127_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='goal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goal.Goal'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
