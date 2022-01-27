from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

from users.forms import UserCreationForm

from django.http import HttpResponse, HttpRequest
from .models import Todo


def list_user_items(request):
    context = {'user_list' : Todo.objects.all()}
    return render(request, 'users/user_list.html',context)


def insert_user_item(request: HttpRequest):
    user = Todo(content=request.POST['content'])
    user.save()
    return redirect('/users/list/')

def delete_user_item(request,user_id):
    user_to_delete = Todo.objects.get(id=user_id)
    user_to_delete.delete()
    return redirect('/users/list/')


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
