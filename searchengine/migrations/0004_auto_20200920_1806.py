# Generated by Django 2.2.7 on 2020-09-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0003_auto_20200919_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porson',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
    ]
