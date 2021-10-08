from django.urls import path
import app.views

urlpatterns = [
    path("hey/", app.views.hey, name="hey"),
    path("", app.views.root, name="root"),
    path("age-in/", app.views.age_in, name="age-in"),
    path("order-total/", app.views.order, name="order-total")
]
