from django.contrib import admin
from django.urls import path, include
from traffic import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('traffic.urls')),

]
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "DITCS Admin"
admin.site.site_title = "DITCS Admin Portal"
admin.site.index_title = "Welcome to DITCS Portal"