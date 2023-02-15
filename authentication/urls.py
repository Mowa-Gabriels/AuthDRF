
from django.urls import path
from .views import (RegisterView, 
                    VerifyEmailView, 
                    LoginAPIView, PasswordTokenCheckAPIView,
                      RequestPasswordReset, SetNewPasswordAPIView)
from rest_framework_simplejwt.views import TokenRefreshView




urlpatterns = [

   path('register/', RegisterView.as_view(), name='register'),
   path('verify-email/', VerifyEmailView.as_view(), name='verify-email'), 

   path('login/', LoginAPIView.as_view(), name='login'),  
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
   path('api/request-rest-email/', RequestPasswordReset.as_view(),
         name='request-rest-email'),
   
   path('api/password-reset/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(),
         name='password-reset-confirm'),

   path('api/password-reset/complete/', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
]

