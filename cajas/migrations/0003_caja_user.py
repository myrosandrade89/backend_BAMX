# Generated by Django 4.1.7 on 2023-03-06 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cajas', '0002_alter_caja_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='caja',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caja', to=settings.AUTH_USER_MODEL),
        ),
    ]
