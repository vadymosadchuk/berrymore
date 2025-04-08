"""berrymore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import (ClientGroupCreateView, ClientCreateView, ProductCreateView, VisitCreateView, PaymentCreateView,
                       UserCreateView, view_index, view_client_details, view_report_index, view_report_daily,
                       view_report_visit)
from app.auth import LoginView, LogoutView


app_name = 'app'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_index, name='index'),
    path('client/<str:client_id>/', view_client_details, name='client_details'),
    path('report/', view_report_index, name='report_index'),
    path('report/daily/<str:date>/', view_report_daily, name='report_daily'),
    path('report/visit/<str:visit_id>/', view_report_visit, name='report_visit'),
    path('add_client/', ClientCreateView.as_view(), name='add_client'),
    path('add_group/', ClientGroupCreateView.as_view(), name='add_group'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('add_visit/', VisitCreateView.as_view(), name='add_visit'),
    path('add_payment/', PaymentCreateView.as_view(), name='add_payment'),
    path('add_user/', UserCreateView.as_view(), name='add_user'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', LoginView.as_view(), name='password_reset'),
]
