from django.urls import path
from .views import *

urlpatterns = [
    path('api/table/', get_company_stocks, name='company-table')
]