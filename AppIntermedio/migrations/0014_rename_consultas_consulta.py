# Generated by Django 4.0.4 on 2022-07-23 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppIntermedio', '0013_consultas_delete_ubicacion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Consultas',
            new_name='Consulta',
        ),
    ]