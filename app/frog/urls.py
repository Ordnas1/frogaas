from django.urls import path, include
from rest_framework.routers import DefaultRouter
from frog import views

router = DefaultRouter()
router.register('frog', views.FrogViewSet)

app_name = "frog"

urlpatterns = [
    path('', include(router.urls))
]
