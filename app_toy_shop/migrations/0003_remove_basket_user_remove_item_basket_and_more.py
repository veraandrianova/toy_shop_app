# Generated by Django 4.0.6 on 2022-08-08 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_toy_shop', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='user',
        ),
        migrations.RemoveField(
            model_name='item',
            name='basket',
        ),
        migrations.RemoveField(
            model_name='item',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='basket',
        ),
        migrations.RemoveField(
            model_name='order',
            name='method_pay',
        ),
        migrations.RemoveField(
            model_name='pay',
            name='address',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Pay',
        ),
    ]