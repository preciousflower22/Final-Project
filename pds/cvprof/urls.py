from django.urls import path
from . import views

app_name = 'cvprof'

urlpatterns = [
    path('<int:id>', views.index, name = "index"),
    path('', views.index, name = "index"),
    path('profiles', views.profile, name = "profiles"),
    path('addprof', views.addprofile, name = "addprof" ),
]
