# Generated by Django 5.0.1 on 2024-01-04 21:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_rename_subject_task_titulo_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="Titulo",
            new_name="titulo",
        ),
        migrations.RemoveField(
            model_name="task",
            name="fecha_creacion",
        ),
        migrations.RemoveField(
            model_name="task",
            name="tarea_completada",
        ),
    ]
