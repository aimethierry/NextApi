from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import CompanyView

urlpatterns = [
    path(r'createCompany/', CompanyView.as_view()),
    path(r'test/', views.test),
]