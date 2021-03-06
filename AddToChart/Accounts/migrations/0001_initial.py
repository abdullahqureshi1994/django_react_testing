# Generated by Django 3.2.7 on 2022-01-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=1000)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Product_Image/')),
                ('Quanity', models.IntegerField(blank=True)),
                ('rate', models.IntegerField(blank=True)),
                ('brand', models.CharField(choices=[('1', 'Local'), ('2', 'Branded'), ('2', 'Imported')], max_length=255)),
            ],
        ),
    ]
