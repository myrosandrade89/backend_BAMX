# Generated by Django 4.1.7 on 2023-03-10 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidades', '0002_alter_comunidad_clave_sae_alter_comunidad_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunidad',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
