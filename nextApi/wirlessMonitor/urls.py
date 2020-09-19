from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import openvpnView, loginCompany, loginEmployee, currentUser, fileView, wifiControl
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path(r'vpn/', openvpnView.as_view()),
    path(r'loginCompany/', loginCompany.as_view()),
    path(r'loginEmployee/', loginEmployee.as_view()),
    path(r'file/', fileView.as_view()),
    path(r'currentlogin/', views.currentUser),
    path(r'wifiControl/', wifiControl.as_view()),
    path(r'api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # path(r'login/', ExampleAuthentication)
]