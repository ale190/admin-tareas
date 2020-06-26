# Generated by Django 3.0.5 on 2020-06-24 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tareas', '0004_auto_20200623_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fechaI', models.DateTimeField(auto_now_add=True)),
                ('fechaF', models.DateTimeField(auto_now_add=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareas.Estado')),
                ('grupoactividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareas.GrupoActividad')),
                ('prioridad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareas.Prioridad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]