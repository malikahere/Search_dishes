# Generated by Django 5.0.7 on 2024-07-13 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='description',
        ),
        migrations.AddField(
            model_name='dish',
            name='location',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='dish',
            name='restaurant_name',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
