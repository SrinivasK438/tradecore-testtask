from rest_framework import serializers

from django.contrib.auth import get_user_model


User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(
        required=True,
        write_only=True,
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
        )
        extra_kwargs = {
            'first_name': {
                'required': True
            },
            'last_name': {
                'required': True
            },
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                "password": "Password fields didn't match."
            })

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            ip_address=self.initial_data['ip_address'],
        )

        return user
