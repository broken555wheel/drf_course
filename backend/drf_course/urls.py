from django.urls import path
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()
# bespoke routers

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]