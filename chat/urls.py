from django.urls import path
from . import views


urlpatterns = [
    path('', views.ChatView.as_view(), name="ChatView"),
    path("chat/<str:room_name>/", views.RoomView.as_view(), name="RoomView"),
]
