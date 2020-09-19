from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import employeeAccountView

urlpatterns = [
    path(r'employeeCompanyAccount/', employeeAccountView.as_view()),
]