# Generated by Django 5.0.4 on 2024-07-05 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_lessonnotes_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonnotes',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_notes', to='core.lesson'),
        ),
    ]
