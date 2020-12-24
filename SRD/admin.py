from django.contrib import admin
from .models import *


admin.site.register(ItemType)
admin.site.register(Item)
admin.site.register(Purchase)
admin.site.register(Rental)

