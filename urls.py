from django.urls import path
from django.views.generic import RedirectView
from . import views  # Import views from the same app

urlpatterns = [
    path('', RedirectView.as_view(url='/weather/', permanent=False)),
    path('weather/', views.weather, name='weather'),
]