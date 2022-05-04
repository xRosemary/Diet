from rest_framework import serializers
from .models import Standard, Nutrition, NutType

class NutTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NutType
        fields = "__all__"

class NutritionModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Nutrition
        fields = "__all__"

class StandardSerializer(serializers.ModelSerializer):
    TypeInfo = NutTypeSerializer()
    nid = NutritionModelSerializer()
    class Meta:
        model = Standard
        fields = "__all__"
