# Generated by Django 3.2 on 2021-04-20 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='№')),
                ('create_date', models.DateTimeField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['create_date'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, verbose_name='Название')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.order')),
            ],
            options={
                'verbose_name': 'Элемент заказа',
                'verbose_name_plural': 'Элементы заказа',
                'ordering': ['order'],
            },
        ),
    ]