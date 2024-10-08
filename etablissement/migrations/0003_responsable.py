# Generated by Django 5.1 on 2024-09-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etablissement', '0002_etablissement_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('signature', models.ImageField(blank=True, null=True, upload_to='')),
                ('profile', models.CharField(max_length=30)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'Responsable',
                'verbose_name_plural': 'Responsables',
                'ordering': ['profile'],
                'indexes': [models.Index(fields=['email'], name='etablisseme_email_642a3e_idx'), models.Index(fields=['telephone'], name='etablisseme_telepho_d70125_idx')],
            },
        ),
    ]
