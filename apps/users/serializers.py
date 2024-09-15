from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = '__all__'


    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = CustomUser.objects.create(**validated_data)
        if profile_data:
            UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        profile = instance.userprofile

        instance.sana_of_tugilgan = validated_data.get('sana_of_tugilgan', instance.sana_of_tugilgan)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.telefon_raqami = validated_data.get('telefon_raqami', instance.telefon_raqami)
        instance.save()

        if profile_data:
            profile.manzil = profile_data.get('manzil', instance.manzil)
            profile.avatar = profile_data.get('avatar', instance.manzil)
            profile.save()

        return instance

