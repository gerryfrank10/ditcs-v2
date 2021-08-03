from django.urls import path, include
from . import views
from rest_framework import routers
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from traffic.views import ChartView

router = routers.DefaultRouter()
router.register(r'traffic', views.TrafficViewSet)
router.register(r'road', views.RoadViewSet)
router.register(r'light', views.LightViewSet)

urlpatterns = [
    path('', ChartView.as_view(), name='index'),
    path('camera/', views.camera, name='camera'),
    path('roads/', views.roads, name='roads'),
    path('roadGerald/', views.roadGerald, name='roadGerald'),
    path('profile/', views.profile, name='profile'),
    path('maps/', views.maps, name='maps'),
    path('updateLight/<str:pk>', views.updateLight, name='updateLight'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.register, name='register'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('api/', include(router.urls)),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/refresh/', TokenRefreshView, name='token_refresh'),
    path('road-export-csv/', views.road_export_csv, name='road_export_csv'),
    path('road-export-excel/', views.road_export_excel, name='road_export_excel'),
    path('genPdf/', views.render_pdf_view, name='render_pdf_view'),
]
