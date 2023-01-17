from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin



class ChatView(LoginRequiredMixin, generic.View):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class RoomView(LoginRequiredMixin, generic.View):
    template_name = 'room.html'    
    def get(self, request, room_name, *args, **kwargs):
        return render(request, self.template_name, {"room_name": room_name})