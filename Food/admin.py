from django.contrib import admin
from .models import Standard, Nutrition, NutType, Composition, Food

class StandardInline(admin.TabularInline):
    model = Standard

class CompositionInline(admin.TabularInline):
    model = Composition

class StandardAdmin(admin.ModelAdmin):
    pass

class NutritionAdmin(admin.ModelAdmin):
    inlines = [StandardInline]
    pass

class NutTypeAdmin(admin.ModelAdmin):
    # inlines = [StandardInline]
    pass

class FoodAdmin(admin.ModelAdmin):
    inlines = [CompositionInline]
    pass

admin.site.register(Standard, StandardAdmin)
admin.site.register(Nutrition, NutritionAdmin)
admin.site.register(NutType, NutTypeAdmin)
admin.site.register(Composition)
admin.site.register(Food, FoodAdmin)