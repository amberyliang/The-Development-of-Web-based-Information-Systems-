# Generated by Django 3.2.25 on 2024-06-20 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_user_id_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='superior',
            field=models.BooleanField(default=False),
        ),
    ]
