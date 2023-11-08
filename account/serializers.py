from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']

        def create(self, validated_data):
            if password is not None:
                password = make_password(validated_data['password'])
            user = User.objects.create(email=validated_data['email'], name=validated_data['name'], password=password)
            print(user.password)
            user.save()
            return user

"""
        def validate_password(self, value: str) -> str:
            \"\"\"
            Hash value passed by user.

            :param value: password of a user
            :return: a hashed version of the password
            \"\"\"
        return make_password(value)
"""
