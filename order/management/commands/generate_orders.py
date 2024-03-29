import random
import pytz
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from order.models import Order, OrderItem


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('num_orders', type=int)

    def handle(self, *args, **options):
        num_orders = options.get('num_orders', 5)
        start_date = datetime(year=2018, month=1, day=1, hour=9, tzinfo=pytz.UTC)
        order_items = []
        for num in range(num_orders):
            date = start_date + timedelta(hours=num)
            num_items = random.randint(1, 5)
            order = Order.objects.create(number=num, create_date=date)
            for n in range(num_items):
                order_items.append(OrderItem(
                    order=order,
                    product_name=f'Товар-{random.randint(1, 100)}',
                    product_price=random.randint(100, 9999),
                    amount=random.randint(1, 10),
                ))
        OrderItem.objects.bulk_create(order_items)
        print('Complete!')
