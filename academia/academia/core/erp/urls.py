from django.urls import path
from core.erp.views import firstview,cursosview

urlpatterns= [
    path('academia/', firstview),
    path('', cursosview)
]