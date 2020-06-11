from django.contrib import admin
from django.urls import path
from places import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('places/<int:pk>/', views.place_info, name='place_info')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
