#from django.conf import settings
#from django.conf.urls.static import static
#from django.urls import path
#from . import views
from typing import List, Union

from django.urls import path, URLResolver, URLPattern
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]

#urlpatterns = [
 #   path('', views.post_list, name='post_list'),
#]
 #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)