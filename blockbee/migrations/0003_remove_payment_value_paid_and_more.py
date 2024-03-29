# Generated by Django 4.1.4 on 2023-01-19 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockbee', '0002_alter_provider_cold_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='value_paid',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='value_received',
        ),
        migrations.AddField(
            model_name='payment',
            name='value_fee_coin',
            field=models.DecimalField(decimal_places=2, default=0, help_text='BlockBee Fee.', max_digits=65, verbose_name='Fee Coin'),
        ),
        migrations.AddField(
            model_name='payment',
            name='value_price',
            field=models.DecimalField(decimal_places=18, default=0, help_text='Coin price in USD at the time of receiving.', max_digits=65, verbose_name='Price Coin in USD'),
        ),
    ]
