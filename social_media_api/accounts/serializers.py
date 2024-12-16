from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user data, including profile details and followers.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['followers']

    def update(self, instance, validated_data):
        # Update the fields based on validated_data
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)

        # Update the password only if provided (hashing automatically handled)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance



class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data):
        # Create the user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Generate a token for the user
        Token.objects.create(user=user)
        return user
    
    def to_representation(self, instance):
        """
        Format the response using the UserSerializer and include the token.
        """
        user_data = UserSerializer(instance).data
        # user_data['token'] = instance.auth_token.key  # Include the generated token
        return {'user_info': user_data,
                'token': instance.auth_token.key }
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following']