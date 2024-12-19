from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('businessPortfolio.urls')),  # Include URLs from your app
]
