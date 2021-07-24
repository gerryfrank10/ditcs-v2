from django.contrib import admin
from .models import  Traffic, Light, Road, Junction
#from .reports import MyReport

@admin.register(Traffic)
class TrafficAdmin(admin.ModelAdmin):
    list_display = ('count', 'road', 'status')
    list_filter = ('time','status' )

@admin.register(Light)
class LightAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    list_filter = ('state', )


@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction', 'junction','state')
    list_filter = ('junction','state')

@admin.register(Junction)
class JunctionAdmin(admin.ModelAdmin):
    list_display = ('name','date')
    list_filter = ('name',)




#reports.register(Road, MyReport)