from django.contrib import admin
from django.urls import path,include
from wonderwebportal.view import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('getresult',getresult),
    path('submit/',submit),
    path('costs/',cost_view),
    path('themes/',themes_view)
]
