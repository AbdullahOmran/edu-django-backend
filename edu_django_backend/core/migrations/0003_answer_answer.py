# Generated by Django 5.0.4 on 2024-07-03 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_feedback_student_id_remove_question_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
