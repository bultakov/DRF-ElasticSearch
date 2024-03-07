from django.urls import path, include
from rest_framework import routers

from .views import ProductViewSet

router = routers.DefaultRouter()
router.register(prefix="", viewset=ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
