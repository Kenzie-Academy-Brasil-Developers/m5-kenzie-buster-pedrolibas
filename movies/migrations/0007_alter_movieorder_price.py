# Generated by Django 4.1.4 on 2022-12-16 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_alter_movieorder_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieorder',
            name='price',
            field=models.FloatField(max_length=8),
        ),
    ]
