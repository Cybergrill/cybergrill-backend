from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AccountsViewSet

router = DefaultRouter()

router.register("accounts", AccountsViewSet, basename="accounts")

urlpatterns = [
    path("", include(router.urls)),
]