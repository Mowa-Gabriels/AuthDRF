
from django.urls import path
from .views import RegisterView, VerifyEmailView, LoginAPIView
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [

   path('register/', RegisterView.as_view(), name='register'),
   path('verify-email/', VerifyEmailView.as_view(), name='verify-email'), 

   path('login/', LoginAPIView.as_view(), name='login'),
   
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
