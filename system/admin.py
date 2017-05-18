from django.contrib import admin
from django.contrib.auth.models import Group

from rest_framework.authtoken.models import Token

from .models import Region, PeopleCategory, People

admin.site.unregister(Token)
admin.site.unregister(Group)
admin.site.register(Region)
admin.site.register(PeopleCategory)
admin.site.register(People)