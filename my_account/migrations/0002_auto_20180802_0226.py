# Generated by Django 2.0.5 on 2018-08-02 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='date_entered',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]