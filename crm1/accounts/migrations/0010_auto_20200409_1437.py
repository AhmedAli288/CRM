# Generated by Django 3.0.4 on 2020-04-09 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_customer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='users',
        ),
    ]
