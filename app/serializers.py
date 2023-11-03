from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email',)

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class ImageSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Image
        fields = ('id', 'user', 'category', 'title', 'image', 'description', 'like_count','created_at', 'updated_at')


class LikeSerializer(ModelSerializer):
    # user = UserSerializer(read_only=True)
    # image = ImageSerializer(read_only=True)
    class Meta:
        model = Like
        fields = ('id', 'image')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
         write_only=True, required=True, validators=[validate_password]
     )
    # password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "email","password", "first_name","last_name")
       
'''
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user        
'''