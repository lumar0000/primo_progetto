# Generated by Django 4.2.5 on 2023-12-01 08:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_rename_visualizazioni_articolo_visualizzazioni'),
    ]

    operations = [
        migrations.AddField(
            model_name='giornalista',
            name='anno_di_nascita',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]