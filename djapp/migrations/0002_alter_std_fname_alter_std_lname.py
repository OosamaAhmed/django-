# Generated by Django 5.0.6 on 2024-07-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='std',
            name='fname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='std',
            name='lname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
