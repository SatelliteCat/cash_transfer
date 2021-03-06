# Generated by Django 3.0.1 on 2019-12-26 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cash_transfer_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('balance', models.DecimalField(decimal_places=5, max_digits=65)),
                ('currency', models.CharField(max_length=50)),
            ],
        ),
    ]
