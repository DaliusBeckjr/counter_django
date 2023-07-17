from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add_one', views.add_one),
    path('destroy_session', views.destroy_session),
]
