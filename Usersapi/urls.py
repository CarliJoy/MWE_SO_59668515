from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
import Usersapi.viewsets as viewset
import Usersapi.views as view

router = routers.DefaultRouter()
router.register('usersapi', viewset.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('test', view.home)
]
