# Generated by Django 4.0.6 on 2022-08-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_toy_shop', '0003_remove_basket_user_remove_item_basket_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Колличество'),
        ),
    ]
