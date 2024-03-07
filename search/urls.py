from django.urls import path

from .views import SearchProducts

urlpatterns = [
    path("product/<str:query>/", SearchProducts.as_view()),
]
