# Generated by Django 5.0.4 on 2024-07-12 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_randomexam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='course_id',
        ),
    ]
