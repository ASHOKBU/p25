# Generated by Django 3.0.8 on 2020-09-07 14:26

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200907_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[myapp.models.validate_name]),
        ),
    ]
