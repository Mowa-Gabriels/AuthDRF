from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User



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
        fiels = [
            'token'
        ]