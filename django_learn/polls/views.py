from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import Group, User


def index(request):

    u = User.objects.get(pk=1)

    ret = u.groups.add(1)

    print(ret)
