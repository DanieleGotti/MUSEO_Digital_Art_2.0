# Generated by Django 5.0.6 on 2024-06-12 23:45

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
