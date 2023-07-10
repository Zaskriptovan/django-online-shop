from django.db import models
from django.contrib.auth.models import User

from shop.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    total_price = models.PositiveIntegerField(default=0, verbose_name='Общая стоимость')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        ordering = ('time_created',)
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'<{self.user}_cart>'


class CartProduct(models.Model):
    product = models.ForeignKey(Product, related_name='cart_products',
                                on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    several_price = models.PositiveIntegerField(default=0, verbose_name='Цена за количество')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    cart = models.ForeignKey('Cart', related_name='cart_products',
                             on_delete=models.CASCADE, verbose_name='Корзина')

    class Meta:
        ordering = ('time_created',)
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзинах'

    def __str__(self):
        return f'<{self.product}_in_{self.cart}>'
