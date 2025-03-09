from django.urls import path
from .views import *

urlpatterns = [
    path('api/predictions/', get_company_predictions, name='company-predictions'),
    path('api/table/', get_company_table, name='company-table'),
    path('api/db-news/', get_company_news, name='company-news'),
    path('api/stats/', get_company_info, name='company-stats'),
    path('api/codes/', get_codes, name='get-codes'),
]