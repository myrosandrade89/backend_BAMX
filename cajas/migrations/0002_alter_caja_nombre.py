# Generated by Django 4.1.7 on 2023-02-27 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cajas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]