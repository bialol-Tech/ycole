# Generated by Django 5.1 on 2024-09-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0004_etudiant_matricule'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='lieu_de_naissance',
            field=models.CharField(default=-1989, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etudiant',
            name='pays_de_naissance',
            field=models.CharField(default='GABON', max_length=20),
            preserve_default=False,
        ),
    ]
