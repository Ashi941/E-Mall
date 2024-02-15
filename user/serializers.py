#emall/user/serializers.py

from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'email', 'first_name', 'last_name',
                  'mobile', 'user_scope','username')
        extra_kwargs = {
            'username': {'required': True},
            'password': {'write_only': True, 'required': True},
            'email': {'required': False},
            'mobile': {'required': True},
            'user_scope': {'required': False},
        }
    def create(self, validated_data):
        if 'username' not in validated_data:
            raise ValidationError({'username': 'This field is required'})
        return User.objects.create_user(**validated_data)
    

    # Logged user can see his profile on dashboard.
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'uuid', 'first_name', 'last_name', 'email', 'username',
                 'mobile', 'status','created_at')
        
class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id','username','email','first_name','last_name']