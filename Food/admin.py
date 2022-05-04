from django.contrib import admin
from .models import Standard, Nutrition, NutType

class StandardInline(admin.TabularInline):
    model = Standard

# class NutTypeInline(admin.TabularInline):
#     model = NutType


class StandardAdmin(admin.ModelAdmin):
    pass

class NutritionAdmin(admin.ModelAdmin):
    inlines = [StandardInline]
    pass

class NutTypeAdmin(admin.ModelAdmin):
    # inlines = [StandardInline]
    pass

admin.site.register(Standard, StandardAdmin)
admin.site.register(Nutrition, NutritionAdmin)
admin.site.register(NutType, NutTypeAdmin)