from rest_framework.viewsets import ModelViewSet
from .models import Standard, Nutrition, NutType, Composition, Food
from .serializers import StandardSerializer, NutritionModelSerializer, NutTypeSerializer, CompositionSerializer, FoodSerializer
# Create your views here.
class StandardModelViewSet(ModelViewSet):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer

class NutritionModelViewSet(ModelViewSet):
    queryset = Nutrition.objects.all()
    serializer_class = NutritionModelSerializer

class NutTypeModelViewSet(ModelViewSet):
    queryset = NutType.objects.all()
    serializer_class = NutTypeSerializer
        
class CompositionModelViewSet(ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer

class FoodModelViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer