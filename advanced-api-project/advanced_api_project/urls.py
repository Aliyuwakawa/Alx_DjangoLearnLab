from django.contrib import admin
from django.urls import path, include  # Import 'include' to include app-specific URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the 'api' app's URL configurations
]




