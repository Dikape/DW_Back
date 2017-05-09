from django.contrib import admin

from .models import InvestMapLog, InvestMapObject, InvestMapPoint, ObjectHolder
# Register your models here.


class InvestMapPointInline(admin.TabularInline):
    model = InvestMapPoint
    extra = 1
    min_num = 0


class InvestMapObjectAdmin(admin.ModelAdmin):
    inlines = (InvestMapPointInline,)

admin.site.register(InvestMapObject, InvestMapObjectAdmin)
admin.site.register(ObjectHolder)