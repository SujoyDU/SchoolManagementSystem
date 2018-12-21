from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import viewsets

class SnippetViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
