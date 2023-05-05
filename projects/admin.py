from django.contrib import admin

from .models import Project
from .models import Category
from .models import Comment


# Project Admin
class ProjectAdmin(admin.ModelAdmin):
    list_display=('id', 'title','description','category')
    search_fields=('title',)   

admin.site.register(Project,ProjectAdmin)

# Category Admin
class CategorytAdmin(admin.ModelAdmin):
    list_display=('id', 'content','created_at')
    search_fields=('content',) 

admin.site.register(Category)

# Comment Admin
admin.site.register(Comment)

# Register your models here.
