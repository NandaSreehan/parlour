# Generated by Django 5.0.7 on 2024-08-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('flavor', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
