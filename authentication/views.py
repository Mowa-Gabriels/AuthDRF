from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


# Create your views here.

class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('verify-email')
        
        abs_url = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.first_name+ '\nUse the Link below to verify your email \n'+'domain:'+abs_url

        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Email Verification'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmailView(generics.GenericAPIView):
    def get(self):
        pass