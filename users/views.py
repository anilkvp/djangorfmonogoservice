from rest_framework import generics

from .models import User
from .serilalizer import UserSerializer


class CreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
