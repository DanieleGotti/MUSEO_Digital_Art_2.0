# Generated by Django 5.0.6 on 2024-06-20 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_tema_id_remove_tema_numerosale_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='sala',
            table='SALA',
        ),
        migrations.AlterModelTable(
            name='tema',
            table='TEMA',
        ),
    ]
