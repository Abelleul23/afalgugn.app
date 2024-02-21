from django.contrib import admin
from .models import LostItem,FoundItem, ReturnedItem


admin.site.register(LostItem)
admin.site.register(FoundItem)
admin.site.register(ReturnedItem)

