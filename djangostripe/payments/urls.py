from django.urls import path

from . import views
from payments.views import payment_intent

urlpatterns = [
    path('charge/', views.charge, name='charge_url'),
    path('', views.HomePageView.as_view(), name='home'),
	path('payment/', payment_intent),
]