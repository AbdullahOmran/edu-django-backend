# Generated by Django 5.0.4 on 2024-07-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_lessonnotes_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessonnotes',
            old_name='lesson_id',
            new_name='lesson',
        ),
        migrations.RenameField(
            model_name='lessonnotes',
            old_name='created_by',
            new_name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='notes',
            field=models.ManyToManyField(through='core.LessonNotes', to='core.lesson'),
        ),
    ]
