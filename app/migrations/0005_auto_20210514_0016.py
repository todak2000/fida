# Generated by Django 3.2.3 on 2021-05-14 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210509_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='noOfBidders',
            field=models.IntegerField(default=0, max_length=15, verbose_name='No of Bidders'),
        ),
        migrations.AddField(
            model_name='orders',
            name='orderStatus',
            field=models.TextField(default='pending', max_length=15, verbose_name='Order Status'),
        ),
    ]
