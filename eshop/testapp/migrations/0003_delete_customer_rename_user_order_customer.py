# Generated by Django 4.0.4 on 2022-05-21 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_remove_order_customer_order_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
    ]