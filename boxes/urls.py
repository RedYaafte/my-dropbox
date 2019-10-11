from django.urls import path, include

from rest_framework import routers

from .views import BoxViewSet

router = routers.DefaultRouter()
router.register(r'list', BoxViewSet, base_name='list')

urlpatterns = router.urls
