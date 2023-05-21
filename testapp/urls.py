from django.urls import path, include
from .views import EmployeeCBViewSet
from rest_framework.routers import DefaultRouter
routers = DefaultRouter()
routers.register('api', EmployeeCBViewSet)
urlpatterns = [
    path('', include(routers.urls))
]
