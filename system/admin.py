from django.contrib import admin

from .models import Region, PeopleCategory, People

admin.site.register(Region)
admin.site.register(PeopleCategory)
admin.site.register(People)