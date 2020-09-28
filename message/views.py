from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request, 'messages/home.html')

def create_link(request):

    if request.method == "POST":
        name = request.POST['name']
        newuser = UserLink()
        newuser.name = name
        newuser.save()
        return redirect(f'/user/{newuser.id}')

    return render(request, 'messages/create_link.html')

def user(request, pk):
    try:
        currentUser = UserLink.objects.get(pk=pk)
    except:
        return redirect('/')
    return render(request, 'messages/user.html' ,{'user':currentUser})

def feedback(request, pk):
    try:
        currentUser = UserLink.objects.get(pk=pk)
    except:
        return redirect('/')
    
    if request.method == "POST":
        newAnswer = Answer()
        newAnswer.content = request.POST["content"]
        # print(newAnswer)
        newAnswer.save()
        currentUser.answers.add(newAnswer)
        # currentUser
        message = f'Your message send successfully to {currentUser.name}'
        return render(request, 'messages/home.html', {'message':message, 'success_alert':True} )

    return render(request, 'messages/feedback.html' ,{'user':currentUser})

def about(request):
    return render(request, 'messages/about.html')