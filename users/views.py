
from django.core.exceptions import PermissionDenied

from django.shortcuts import redirect

'''
from django.contrib.auth.models import User
from users.forms import SignUpForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
'''
# Create your views here.


def redirect_view(request):
    if request.user.groups.filter(name='Gestor').exists():
        response = redirect('gestor-home')
    elif request.user.groups.filter(name='Operari').exists():
        response = redirect('operaris-notificacions')
    elif request.user.groups.filter(name='Tecnic').exists():
        response = redirect('tecnics-notificacions')
    elif request.user.groups.filter(name='CEO').exists():
        response = redirect('ceo-home')
    else:
        raise PermissionDenied()
    return response
