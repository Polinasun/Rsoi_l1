from django.urls import include, path
from .views import new_car, get_car

urlpatterns = [
    path('new_car/', new_car),
    path('get_car/', get_car),
]
