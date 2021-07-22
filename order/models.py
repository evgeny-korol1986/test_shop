from django.db import models


class Order(models.Model):
    number = models.IntegerField(verbose_name='№')
    create_date = models.DateTimeField(verbose_name='Дата', db_index=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['create_date']

    def __str__(self):
        return f'Order {self.number}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(verbose_name='Название', max_length=255)
    product_price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10)
    amount = models.IntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'
        ordering = ['product_name']

    def __str__(self):
        return self.product_name
