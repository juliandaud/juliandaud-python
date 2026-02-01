from django.urls import path
from . import views

app_name = "mensajes"

urlpatterns = [
    path('', views.InboxView.as_view(), name='inbox'),
    path('new/', views.enviar_mensaje, name='enviar_mensaje'),
    path('dejar/', views.dejar_mensaje, name='dejar_mensaje'),
]