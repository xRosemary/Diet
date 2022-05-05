from rest_framework import serializers
from .models import Standard, Nutrition, NutType, Composition, Food

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
    ageInfo = NutritionModelSerializer()
    class Meta:
        model = Standard
        fields = "__all__"

    
class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = "__all__"
    
class CompositionSerializer(serializers.ModelSerializer):
    type = NutTypeSerializer()
    food = FoodSerializer()
    class Meta:
        model = Composition
        fields = "__all__"