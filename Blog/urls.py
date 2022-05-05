from django.db import router
from rest_framework.routers import DefaultRouter
from Blog import views

router = DefaultRouter()
router.register("category", views.CategoryModelViewSet, basename="category")
router.register("article", views.ArticleModelViewSet, basename="article")
urlpatterns = [] + router.urls
