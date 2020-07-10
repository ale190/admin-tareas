# Generated by Django 3.0.5 on 2020-07-07 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0012_auto_20200626_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='fechaF',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='fechaI',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tareas.Estado'),
        ),
    ]