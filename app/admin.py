from django.contrib import admin

# Register your models here.
from .models import Post, Category


# conf for category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'add_date',)


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'add_date',)


admin.site.register(Post,)
admin.site.register(Category, CategoryAdmin)
