# Generated by Django 2.2.13 on 2021-05-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='no_of_views',
            field=models.IntegerField(default=0, max_length=200, verbose_name='No of Views'),
            preserve_default=False,
        ),
    ]