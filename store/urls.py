from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.request, name='request'),
    path('payment/<int:request_id>/', views.payment, name='payment'),
]
