# Generated by Django 3.0.7 on 2023-10-19 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20231018_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(default=1, upload_to='company_logos/'),
            preserve_default=False,
        ),
    ]
