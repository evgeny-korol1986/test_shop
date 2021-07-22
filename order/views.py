import pytz
from datetime import datetime
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models.functions import JSONObject
from django.db.models import Sum, F
from django.views.generic.list import ListView
from .models import Order, OrderItem
from .utils import ReportFormMixin
from .forms import OrderReportForm, ProductReportForm


class OrderReportView(ReportFormMixin, ListView):
    template_name = 'order/orders.html'
    model = Order
    paginate_by = 10
    form_class = OrderReportForm

    def get_queryset(self):
        date_range = self.get_date_range(self.get_filter_params())
        queryset = self.model.objects.filter(create_date__range=date_range).annotate(
            total_price=Sum(F('orderitem__product_price') * F('orderitem__amount')),
            items=ArrayAgg(JSONObject(product_name='orderitem__product_name', amount='orderitem__amount')),
        ).order_by('create_date')
        return list(queryset)


class ProductReportView(ReportFormMixin, ListView):
    template_name = 'order/products.html'
    model = OrderItem
    paginate_by = 10
    form_class = ProductReportForm
    initial = {
        'top': 20,
        'start_date': datetime(year=2018, month=1, day=1, tzinfo=pytz.UTC),
        'end_date': datetime(
            year=2018, month=1, day=2, hour=23, minute=59, second=59, microsecond=999999, tzinfo=pytz.UTC),
    }

    def get_queryset(self):
        filter_params = self.get_filter_params()
        date_range = self.get_date_range(filter_params)
        top = filter_params['top']
        queryset = self.model.objects.filter(order__create_date__range=date_range).values('product_name').annotate(
            total=Sum('amount'),
            orders=ArrayAgg(JSONObject(number='order__number', create_date='order__create_date', price='product_price')),
        ).order_by('-total')[:top]
        return list(queryset)
