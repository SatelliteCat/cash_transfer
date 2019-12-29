from django.urls import path
from cash_transfer_app import views

urlpatterns = [
    path('api/v1/transfer', views.transfer_api),
]