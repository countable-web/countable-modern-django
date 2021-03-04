from django.contrib import admin

from web.models import AppModel

# Register your models in the Django admin view here.


@admin.register(AppModel)
class AppModelAdmin(admin.ModelAdmin):
    model = AppModel
    list_display = ("id",)
