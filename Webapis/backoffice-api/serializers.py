# Thrid-party Libraries
from rest_framework import serializers

# Own's Libraries
from Business.controllers import BackofficeWeb


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackofficeWeb.UserModel
        fields = (
            'id',
            'name',
            'email',
            'is_active',
            'is_verified',
        )
