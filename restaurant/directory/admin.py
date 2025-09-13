from django.contrib import admin
from .models import Restaurant, Place, Food, Chef
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Place)
admin.site.register(Food)
admin.site.register(Chef)
