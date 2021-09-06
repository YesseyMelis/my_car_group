from django.urls import path

from apps.core.views import GetCarView

urlpatterns = [
    path('cars', GetCarView.as_view(), name='get_cars'),
]

app_name = 'core'
