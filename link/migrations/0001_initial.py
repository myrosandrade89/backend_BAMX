# Generated by Django 4.1.7 on 2023-03-08 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liga', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ['liga'],
            },
        ),
    ]
