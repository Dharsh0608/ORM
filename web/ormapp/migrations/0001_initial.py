# Generated by Django 5.1.2 on 2024-10-28 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('accountnumber', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('income', models.IntegerField()),
                ('security', models.CharField(max_length=6)),
                ('intrest', models.IntegerField()),
            ],
        ),
    ]