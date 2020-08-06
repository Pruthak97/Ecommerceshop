from django.contrib import admin

from .models import Products, PostImage


# Register your models here.

class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Products)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Products


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
