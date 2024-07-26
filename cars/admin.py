from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.car est le nom du model qu'on veux voir  dans la parti admin

class CarAdmin(admin.ModelAdmin):

        def thumbnail(self,object):
            return format_html('<img src="{}" width="40" style="border-radius: 50px;"  />'.format(object.car_photo.url))

        thumbnail.short_description = 'Car Image'
        list_display=('id','thumbnail','car_title','color','modele','year','body_style','fuel_type','is_featured')
        list_display_links=('id','thumbnail','car_title')
        list_editable=('is_featured',)
        search_fields = ('car_title' ,'modele' , 'body_style')
        list_filter =('modele','city')
#
#
admin.site.register(Car,CarAdmin)
