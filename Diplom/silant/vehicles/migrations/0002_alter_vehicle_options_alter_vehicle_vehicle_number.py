# Generated by Django 4.2.7 on 2023-11-21 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name': 'Техника', 'verbose_name_plural': 'Техника'},
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_number',
            field=models.CharField(max_length=12, unique=True, verbose_name='Зав. № техники'),
        ),
    ]