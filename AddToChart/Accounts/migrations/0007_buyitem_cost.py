# Generated by Django 3.2.7 on 2022-01-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_buyitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyitem',
            name='cost',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
