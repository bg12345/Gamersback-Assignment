# Generated by Django 3.1.7 on 2021-07-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldhappinessreport',
            name='countryName',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='worldhappinessreport',
            name='gdp',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='worldhappinessreport',
            name='generosity',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='worldhappinessreport',
            name='healthyLifeExpectancy',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='worldhappinessreport',
            name='ladderScore',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='worldhappinessreport',
            name='rank',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]