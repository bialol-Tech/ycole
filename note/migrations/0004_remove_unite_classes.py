# Generated by Django 5.1 on 2024-08-27 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_remove_semestre_actif_remove_semestre_debut_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unite',
            name='classes',
        ),
    ]
