from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from rest_framework import viewsets
from users.models import CustomUser
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly

class SnippetViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

