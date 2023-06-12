from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # admin 으로 들어오는 url 외에는 아래 path로 redirect
    path('', include('board_main.urls')),
]
