# Generated by Django 4.0.6 on 2022-07-29 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_toy_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_admin_room', to=settings.AUTH_USER_MODEL, verbose_name='Администратор'),
        ),
        migrations.AddField(
            model_name='room',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_room', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reviews', to='app_toy_shop.product', verbose_name='Продукт'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_reviews', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_product', to='app_toy_shop.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='pay',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_pay', to='app_toy_shop.address', verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='order',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_order', to='app_toy_shop.basket', verbose_name='Корзина'),
        ),
        migrations.AddField(
            model_name='order',
            name='method_pay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pay_order', to='app_toy_shop.pay', verbose_name='Метод оплаты'),
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='number_room', to='app_toy_shop.room', verbose_name='Комната'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_message', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='item',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_item', to='app_toy_shop.basket', verbose_name='Корзина'),
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_item', to='app_toy_shop.product', verbose_name='Продукт'),
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='app_toy_shop.product', verbose_name='Продукт'),
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_basket', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]