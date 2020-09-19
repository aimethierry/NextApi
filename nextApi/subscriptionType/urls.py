from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import SubscriptionType

urlpatterns = [
    path(r'createtype/', SubscriptionType.as_view()),
]