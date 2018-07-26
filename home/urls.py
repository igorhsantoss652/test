from django.urls import path
from .views import home
from .views import index
from django.contrib.auth.views import login, logout
urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('index/', index, name="index"),
]
