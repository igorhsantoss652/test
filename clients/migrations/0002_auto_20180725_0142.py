# Generated by Django 2.0.7 on 2018-07-25 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='cnpj',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
