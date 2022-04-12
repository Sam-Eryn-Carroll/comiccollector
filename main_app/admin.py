from django.contrib import admin

from .models import Comic, Review

admin.site.register(Comic)

admin.site.register(Review)