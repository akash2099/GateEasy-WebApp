from django.contrib import admin

# Register your models here.
from .models import MockTest

admin.site.register(MockTest)