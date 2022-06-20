from django.urls import path

from .views import home, details

urlpatterns = [
    path('home', home, name = 'home'),
    path('<int:id>', details, name = 'details'),
]
