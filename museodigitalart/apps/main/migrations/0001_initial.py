# Generated by Django 4.1.13 on 2024-06-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codice', models.IntegerField()),
                ('descrizione', models.CharField(max_length=255)),
                ('numeroSale', models.IntegerField()),
            ],
        ),
    ]