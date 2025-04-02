# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog  # Import your model

admin.site.register(Blog)  # Register the model

