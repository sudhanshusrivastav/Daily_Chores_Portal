# Generated by Django 5.0.1 on 2024-04-10 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcs_app', '0004_alter_hiring_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='comp_reg',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
