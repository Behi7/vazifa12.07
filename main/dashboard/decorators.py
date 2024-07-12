from main import models
from django.shortcuts import render, redirect

def is_owner(funk):
    def wrapper(request, id):
        if request.user == models.Blog.objects.get(id=id).author:
            return funk(request, id)
        else:
            return redirect('index')
    return wrapper