from django.urls import path
from core.erp.views import firstview

urlpatterns= [
    path('academia/', firstview)
    
]