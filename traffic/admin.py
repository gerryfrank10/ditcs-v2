from django.contrib import admin
from .models import  Traffic, Light, Road, Junction, People
#from .reports import MyReport

@admin.register(Traffic)
class TrafficAdmin(admin.ModelAdmin):
    list_display = ('count', 'road', 'status')
    list_filter = ('time','status' )

@admin.register(Light)
class LightAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'road')
    list_filter = ('state','road' )


@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction', 'junction',)
    list_filter = ('junction',)

@admin.register(Junction)
class JunctionAdmin(admin.ModelAdmin):
    list_display = ('name','date')
    list_filter = ('name',)

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'user')
    list_filter = ('age',)


#reports.register(Road, MyReport)