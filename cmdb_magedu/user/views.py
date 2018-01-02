from django.shortcuts import render, redirect
from django.http import HttpResponse

import time

def index_v1(request):
    html = '''
        
    
    '''
    return HttpResponse(html)

def index(request):
    print(request.GET, request.POST)
    context = {
        'name': request.GET.get('name'),
    }
    return render(request, 'user/login.html', context)


def login(request):
    print(request.GET, request.POST)
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')
    if name == 'miracle' and password == 'cmdb':
        return redirect('user:users')
    else:
        context = {}
        context['name'] = name
        context['errors'] = ['用户名或密码错误']
        return render(request, 'user/login.html', context)


def users(request):
    context = {
        'data': [
            {'name': 'miracle', 'age': 18, 'telephone': 13916227150, 'email': 'miracle@gmail.com', 'register_time': time.time()},
        ]
    }
    return render(request, 'user/users.html', context)