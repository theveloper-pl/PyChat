from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import auth

class LoginPageView(generic.View):
    template_name = 'login.html'
    
    def get(self, request):
        return render(request, self.template_name)
        
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        
        print(email, password, )

        if user is not None:
            auth.login(request, user)
            return redirect('ChatView')
        else:
            return redirect('LoginPageView')
