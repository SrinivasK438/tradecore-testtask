from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from users.serializers import SignupSerializer


class SignupView(generics.CreateAPIView):

    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        request.data.update({'ip_address': request.META['REMOTE_ADDR']})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response = {
            'email': serializer.data['email'],
            'first_name': serializer.data['first_name'],
            'last_name': serializer.data['last_name'],
        }
        return Response(
            response,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


signup_view = SignupView.as_view()
