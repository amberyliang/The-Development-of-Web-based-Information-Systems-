# Generated by Django 3.2.25 on 2024-06-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_auto_20240619_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id_number',
            field=models.CharField(default='a100000000', max_length=10),
        ),
    ]
