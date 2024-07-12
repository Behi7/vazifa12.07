from main import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from decorators import *

@login_required(login_url='index')
def blog_create(request):
    if request.method == 'POST':
        models.Blog.objects.create(
            author = request.user,
            title = request.POST['title'],
            body = request.POST['body'],
            image = request.FILES['image']
        )
        return redirect('index')
    return render(request, 'dashboard/create-blog.html')


# @login_required
# def blog_update(request, id):
#     blog = models.Blog.objects.get(id=id)
#     if request.method == 'POST':
#             blog.title = request.POST['title']
#             blog.body = request.POST['body']
#             blog.image = request.FILES['image']
#             blog.image = blog.image
#             blog.save()
#     return render(request, 'dashboard/update-blog.html', {'blog':blog})

@is_owner
@login_required
def blog_update(request, id):
    blog = models.Blog.objects.get(id=id)
    original_image = blog.image
    print(request.user)

    if request.method == 'POST':
        form_data = request.POST
        image_file = request.FILES.get('image')

        blog.title = form_data['title']
        blog.body = form_data['body']
        blog.image = image_file or original_image
        blog.save()
    return render(request, 'dashboard/update-blog.html', {'blog': blog})


@is_owner
@login_required
def blog_delete(request, id):
    models.Blog.objects.get(id=id).delete()
    return redirect('index')


@login_required
def my_blogs(request):
    blogs = models.Blog.objects.filter(author = request.user)
    return render(request, 'dashboard/list-blogs.html', {'blogs':blogs})

