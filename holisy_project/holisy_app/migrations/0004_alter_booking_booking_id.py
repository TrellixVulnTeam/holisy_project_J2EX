# Generated by Django 3.2.4 on 2021-06-10 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holisy_app', '0003_alter_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
