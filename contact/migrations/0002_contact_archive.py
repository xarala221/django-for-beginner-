# Generated by Django 2.2.7 on 2019-12-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
