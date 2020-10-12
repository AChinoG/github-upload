# Generated by Django 3.1.1 on 2020-09-25 21:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notas',
            name='identifcador',
        ),
        migrations.AddField(
            model_name='notas',
            name='autor',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
