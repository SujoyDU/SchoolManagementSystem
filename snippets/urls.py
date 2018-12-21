from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
