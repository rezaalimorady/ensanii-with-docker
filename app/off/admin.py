from django.contrib import admin
from .models import Off, UseCodeByUser


# Register your models here.
class OffAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """save current user as author"""
        obj.ctrated_by = request.user
        obj.save()

    readonly_fields = ('ctrated_by',)
    list_display = ('name', 'code', 'status', 'date_create', 'expired_at', 'ctrated_by',)
    list_filter = ('status', 'date_create', 'expired_at',)
    search_fields = ('name', 'code',)


admin.site.register(Off, OffAdmin)


class UseCodeByUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """save current user as author"""
        obj.user = request.user
        obj.save()

    list_display = ('code', 'user')



admin.site.register(UseCodeByUser, UseCodeByUserAdmin)
