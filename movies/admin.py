from django.contrib import admin

# Register your models here.
from .models import Movie, Review
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Movie, MovieAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'comment', 'is_approved', 'date')
    list_filter = ('is_approved', 'date')
    list_editable = ('is_approved',)
admin.site.register(Review, ReviewAdmin)