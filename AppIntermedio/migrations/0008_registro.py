# Generated by Django 4.0.4 on 2022-07-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppIntermedio', '0007_contacto_titulo_alter_libro_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
        ),
    ]
