# Generated by Django 5.1.4 on 2025-01-26 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tarea', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={},
        ),
        migrations.AlterModelTable(
            name='category',
            table='Categories',
        ),
        migrations.AlterModelTable(
            name='project',
            table='Projects',
        ),
        migrations.AlterModelTable(
            name='tag',
            table='Tags',
        ),
        migrations.AlterModelTable(
            name='technology',
            table='Technologies',
        ),
    ]
