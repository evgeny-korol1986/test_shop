from django.urls import path
from .views import OrderReportView, ProductReportView


urlpatterns = [
    path('', OrderReportView.as_view(), name='orders'),
    path('products/', ProductReportView.as_view(), name='products'),
]
