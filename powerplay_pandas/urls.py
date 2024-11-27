from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('league-sphere/', include('league_sphere.urls')),  # Include the URLs from the league_sphere app.
    path('organisations/', include('organisations.urls')),  # Include the URLs from the organisations app.
    path('common/', include('common.urls')),  # Include the URLs from the common app.
]