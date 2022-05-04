from rest_framework.viewsets import ModelViewSet
from .models import Standard, Nutrition, NutType
from .serializers import StandardSerializer, NutritionModelSerializer, NutTypeSerializer
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