# Generated by Django 3.2.7 on 2022-01-29 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_buyitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyitem',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
