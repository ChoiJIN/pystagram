# coding: utf-8

from django.contrib import admin

from photo.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'image_file', 'filtered_image_file']

admin.site.register(Photo, PhotoAdmin)
