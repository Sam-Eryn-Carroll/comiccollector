from django.contrib import admin

from .models import Comic, Review, Character

admin.site.register(Comic)

admin.site.register(Review)

admin.site.register(Character)