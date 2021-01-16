from django.conf import settings
from django.conf.urls.static import static
#from django.urls import path
#from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

#urlpatterns = [
 #   path('', views.post_list, name='post_list'),
#]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)