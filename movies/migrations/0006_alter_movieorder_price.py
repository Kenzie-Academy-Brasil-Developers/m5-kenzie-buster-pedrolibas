# Generated by Django 4.1.4 on 2022-12-16 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieorder',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
