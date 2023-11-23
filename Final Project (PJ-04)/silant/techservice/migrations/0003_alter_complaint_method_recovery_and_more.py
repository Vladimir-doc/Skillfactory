# Generated by Django 4.2.7 on 2023-11-21 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_alter_vehicle_options_alter_vehicle_vehicle_number'),
        ('techservice', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='method_recovery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='techservice.recoverymethod', verbose_name='Способ восстановления'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle', verbose_name='Техника'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle', verbose_name='Техника'),
        ),
    ]