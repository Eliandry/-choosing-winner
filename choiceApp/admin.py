from django.contrib import admin
from .models import *

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['name','author']
    list_filter = ['author',]

admin.site.register(Photo)



