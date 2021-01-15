from django.urls import path
from . import views
from .views import post_list

app_name = 'core'

urlpatterns = [
    path('post', post_list, name = "blog"),  #blog/plot

]

