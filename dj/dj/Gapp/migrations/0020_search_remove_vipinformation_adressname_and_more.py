# Generated by Django 4.2.1 on 2023-08-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gapp', '0019_delete_adress_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.CharField(default='', max_length=500)),
                ('latitude', models.CharField(default='', max_length=500)),
                ('AdressName', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='vipinformation',
            name='AdressName',
        ),
        migrations.RemoveField(
            model_name='vipinformation',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='vipinformation',
            name='longitude',
        ),
        migrations.AddField(
            model_name='vipinformation',
            name='VIPInformation_Collect',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='vipinformation',
            name='VIPInformation_Feadback',
            field=models.CharField(default='', max_length=200),
        ),
    ]
