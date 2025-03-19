from .views import *
from django.urls import path

urlpatterns = [
    path('update/table/', update_company_table, name='update-company'),
]