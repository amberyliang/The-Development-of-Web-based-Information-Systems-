# Generated by Django 3.2.19 on 2023-06-12 18:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('department', models.CharField(choices=[('小兒科', '小兒科'), ('婦產科', '婦產科'), ('外科', '外科'), ('內科', '內科')], max_length=10)),
            ],
        ),
    ]
