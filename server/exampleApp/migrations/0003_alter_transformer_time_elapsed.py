# Generated by Django 4.0.4 on 2023-04-30 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exampleApp', '0002_transformer_delete_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transformer',
            name='timeElapsed',
            field=models.FloatField(),
        ),
    ]
