from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", app.views.root, name="root"),
    path("hey/", app.views.hey, name="hey")
]
