# Generated by Django 5.0.1 on 2024-04-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrent', '0002_alter_booking_pick_up_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='pick_up_date',
            field=models.DateField(null=True),
            preserve_default=False,
        ),
    ]