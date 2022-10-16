from django.contrib import admin

# Register your models here.
from .models import Director, Movie, Meta

admin.site.register(Director)
admin.site.register(Meta)
admin.site.register(Movie)
