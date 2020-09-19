from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import CompanyAccountView

urlpatterns = [
    path(r'createCompanyAccount/', CompanyAccountView.as_view()),
]