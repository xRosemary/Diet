from django.contrib import admin
from .models import UserInfo, HealthRecord, IllnessMode
# Register your models here.

class HealthRecordInline(admin.StackedInline):
    model = HealthRecord

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['userName', 'age', 'gender', 'phone_number']
    inlines = [HealthRecordInline]

class HealthRecordAdmin(admin.ModelAdmin):

    list_display = ['username']

    def username(self, obj):
        return obj.user.userName

    exclude = ['user']

class IllnessModeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(HealthRecord, HealthRecordAdmin)
admin.site.register(IllnessMode, IllnessModeAdmin)