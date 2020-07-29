from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('offcode', views.OffView)
router.register('UsedByUser', views.UseCodeByUserView)

app_name = 'off'
urlpatterns = [
    path('', include(router.urls))
]