# Generated by Django 4.1.7 on 2023-03-16 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0003_alter_turno_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='nombre_comunidad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
