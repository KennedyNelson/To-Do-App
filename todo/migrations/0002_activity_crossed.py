# Generated by Django 2.2.6 on 2020-04-27 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='crossed',
            field=models.BooleanField(default=False),
        ),
    ]