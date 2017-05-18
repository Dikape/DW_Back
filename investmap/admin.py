from django.contrib import admin

from investmap.models import OwnershipForm, ObjectHolder, ContractType, ObjectCategory, InvestmentObject, InvestMapPoint


class InvestMapPointInline(admin.TabularInline):
    model = InvestMapPoint
    extra = 1
    min_num = 0


class InvestmentObjectAdmin(admin.ModelAdmin):
    inlines = (InvestMapPointInline,)

admin.site.register(InvestmentObject, InvestmentObjectAdmin)
admin.site.register(OwnershipForm)
admin.site.register(ObjectHolder)
admin.site.register(ContractType)
admin.site.register(ObjectCategory)