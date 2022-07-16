from django.db import router
from rest_framework.routers import DefaultRouter
from Food import views

router = DefaultRouter()
router.register("standard", views.StandardModelViewSet, basename="standard")
router.register("nutrition", views.NutritionModelViewSet, basename="nutrition")
router.register("type", views.NutTypeModelViewSet, basename="type")
router.register("composition", views.CompositionModelViewSet, basename="composition")
router.register("food", views.FoodModelViewSet, basename="food")
urlpatterns = [] + router.urls
