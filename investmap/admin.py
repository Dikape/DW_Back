from django.contrib import admin

from .models import InvestMapLog, InvestmentObject, InvestMapPoint, ObjectHolder
# Register your models here.


class InvestMapPointInline(admin.TabularInline):
    model = InvestMapPoint
    extra = 1
    min_num = 0


class InvestmentObjectAdmin(admin.ModelAdmin):
    inlines = (InvestMapPointInline,)

admin.site.register(InvestmentObject, InvestmentObjectAdmin)
admin.site.register(ObjectHolder)