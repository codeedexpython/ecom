from django.contrib import admin

# Register your models here.
from .models import Tag,Category

# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)
