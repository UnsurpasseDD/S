from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class CategoryAdmin(TranslationAdmin):
    model = Category


class PostAdmin(TranslationAdmin):
    model = Post


def nullfy_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


nullfy_quantity.short_description = 'Обнулить Посты'


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'category']
    list_filter = ['author', 'category']
    search_fields = ['author', 'category']
    actions = [nullfy_quantity]


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
# Register your models here.
