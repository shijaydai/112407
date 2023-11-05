# Generated by Django 4.2.5 on 2023-11-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='effective',
            fields=[
                ('storeid', models.IntegerField(primary_key=True, serialize=False)),
                ('eff', models.CharField(max_length=10)),
                ('noeff', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placename', models.CharField(max_length=300)),
                ('placeaddress', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('feadback', models.CharField(max_length=300)),
                ('recommend', models.CharField(max_length=300)),
            ],
        ),
    ]
