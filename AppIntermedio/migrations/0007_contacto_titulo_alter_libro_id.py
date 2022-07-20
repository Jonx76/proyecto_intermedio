# Generated by Django 4.0.5 on 2022-07-20 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppIntermedio', '0006_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='titulo',
            field=models.CharField(default=1, max_length=100, verbose_name='Título'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='libro',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
