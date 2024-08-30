# api/urls.py
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]


from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is imported
from rest_framework.routers import DefaultRouter
from api.views import BookViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Use the router's URLs
]

