from django.urls import path
from .  import views
urlpatterns = [
    path('',views.home, name='home'),
    path('eggs/',views.eggs),
    path('countggg/',views.count,name='count'),
    path('about/',views.about,name='about')
]
