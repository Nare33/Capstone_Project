from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, DiaryEntryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'diary-entries', DiaryEntryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

