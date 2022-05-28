from django.contrib import admin

from .models import ItemModel
from .models import TestModel

admin.site.register(ItemModel)
admin.site.register(TestModel)
