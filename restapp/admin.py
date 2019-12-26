from django.contrib import admin

from .models import CustomUser,Person , Address



admin.site.register(Address)
admin.site.register(Person)
admin.site.register(CustomUser)


