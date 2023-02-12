from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User
from django.contrib.auth import authenticate, login
from rest_framework.exceptions import AuthenticationFailed



class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(
        min_length=6, max_length=70, write_only=True)
    
    class Meta:
        model = User
        fields = [
            "email","first_name", "password"
        ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        first_name = attrs.get('first_name', '')

        if not first_name.isalnum():
            raise serializers.ValidationError("Useranme should only contain alphanumerals")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
    
        return user
    
class VerifyEmailSerializer(ModelSerializer):

    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = [
            'token'
        ]


class LoginSerializer(ModelSerializer):
    email = serializers.EmailField(min_length=6, max_length=70)
    password = serializers.CharField(
        min_length=6, max_length=70, write_only=True)
    tokens = serializers.CharField(
        min_length=6, read_only=True)
    first_name = serializers.CharField(
        min_length=6, max_length=70, read_only=True)
    
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'tokens',
            'password',
        ]
    


    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid Credentials')
       
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified, Contact admin')
           
        if not user.is_active:
            raise AuthenticationFailed('Account not active')
        

        return{
            'email':user.email,
            'first_name':user.first_name,
            'tokens': user.tokens()
        }

        