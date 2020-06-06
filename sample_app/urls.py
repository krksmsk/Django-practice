from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/',include('hello_world.urls')),
]
