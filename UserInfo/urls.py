from django.db import router
from rest_framework.routers import DefaultRouter
from UserInfo import views

router = DefaultRouter()
router.register("users", views.UserInfoModelViewSet, basename="users")
router.register("health", views.HealthRecordModelViewSet, basename="health")
urlpatterns = [] + router.urls
