# Generated by Django 4.1.2 on 2022-12-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_logins_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=120, null=True)),
                ('speed', models.CharField(max_length=15)),
                ('s_speed', models.CharField(max_length=12, null=True, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Logins',
        ),
    ]
