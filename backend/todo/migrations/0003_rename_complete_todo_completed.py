# Generated by Django 5.0.4 on 2024-04-18 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='complete',
            new_name='completed',
        ),
    ]
