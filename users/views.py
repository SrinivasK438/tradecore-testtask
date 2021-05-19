from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from users.serializers import SignupSerializer


class SignupView(generics.CreateAPIView):

    serializer_class = SignupSerializer

    def perform_create(self, serializer):
        serializer.save(
            ip_address=self.request.META['REMOTE_ADDR']
        )


signup_view = SignupView.as_view()
