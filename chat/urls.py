from django.urls import path
from .views import hacer_pregunta, clear 

urlpatterns = [
    path('chat/', hacer_pregunta, name='chat_view'),
    path('clear/', clear, name='clear_view'),
]