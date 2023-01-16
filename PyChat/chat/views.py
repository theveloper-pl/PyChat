from django.shortcuts import render
from django.views import generic




class ChatView(generic.View):
    def get(self, request, *args, **kwargs):
        template_name = 'chat.html'
        return render(request, template_name)
    


