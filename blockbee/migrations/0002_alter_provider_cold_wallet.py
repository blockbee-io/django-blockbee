# Generated by Django 4.1.4 on 2023-01-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockbee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='cold_wallet',
            field=models.CharField(blank=True, help_text='Address can be set here or in the BlockBee Dashboard.', max_length=128, verbose_name='Cold Wallet'),
        ),
    ]
