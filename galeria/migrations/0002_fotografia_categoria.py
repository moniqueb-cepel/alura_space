# Generated by Django 5.1.7 on 2025-04-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('PALNETA', 'Planeta')], default='', max_length=100),
        ),
    ]
