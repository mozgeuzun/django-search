import imp
from pprint import pprint
from django.shortcuts import render, redirect
import urllib.request
from django.http import HttpResponse, request, response
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.http import JsonResponse 
from .db import db
import json
 
def index(request: request):
    if "user" in request.session:
        return render(request, 'user/index.html', {'title':'index'})
    else:
        return redirect('login')

def Login(request):
    if request.method == 'POST':  
        username = request.POST['username']
        password = request.POST['password']
        ##user = authenticate(request, username = username, password = password)
        if 1 == 1:
            #form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            request.session["user"] = username
            return redirect('index')
        else:
            messages.info(request, f'ACCOUNT DOESNT EXIST')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})

def Logout(request:request):
    if "user" in request.session:
        del request.session["user"]
    return redirect('login')

def liste(request: request):
    l = db.liste()
    return HttpResponse(json.dumps(l))

def delete(request:request,id):
    return HttpResponse(json.dumps(db.delete(id)))
    #return render(request, 'user/liste.html', {'title':'liste'})

def add(request:request):
    data = json.loads(request.body.decode('utf-8'))
    result = db.add(data["fnamestudent"],data["lnamestudent"],data["department"])
    return  JsonResponse({ "result" : result})
    

