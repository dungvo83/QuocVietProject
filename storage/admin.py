from django.contrib import admin
from storage.models import Category, Item, ItemAction


# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemAction)
