# Generated by Django 2.0.2 on 2018-02-24 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20180223_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
