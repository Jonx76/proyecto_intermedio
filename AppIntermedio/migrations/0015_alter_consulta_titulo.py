# Generated by Django 4.0.4 on 2022-07-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppIntermedio', '0014_rename_consultas_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Deje aqui su consulta'),
        ),
    ]
