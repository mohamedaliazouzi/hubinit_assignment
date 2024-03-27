from django.shortcuts import render, redirect
from .models import Blog

# Create your views here.


def redirect_to_blog(request):
    return redirect('blog')  # Redirect to the 'blog' named URL pattern


def blog(request):
    items = Blog.objects.all()
    return render(request, "blog.html", {"blogs": items})


def add(request):
    return render(request, "add.html")


def addrec(request):
    x = request.POST['blog_title']
    y = request.POST['blog_text']
    z = request.POST['blog_status']
    author_name = request.user  # Assuming author_name is a ForeignKey to the User model
    b = Blog(blog_title=x, blog_status=z,
             blog_text=y, author_name=author_name)
    b.save()
    return redirect("blog")


def delete(request, id):
    b = Blog.objects.get(id=id)
    b.delete()
    return redirect("blog")


def update(request, id):
    b = Blog.objects.get(id=id)
    return render(request, "update.html", {'blog': b})


def uprec(request, id):
    x = request.POST['blog_title']
    y = request.POST['blog_text']
    z = request.POST['blog_status']
    author_name = request.user  # Assuming author_name is a ForeignKey to the User model
    b = Blog.objects.get(id=id)
    b.blog_title = x
    b.blog_status = z
    b.blog_text = y
    b.author_name = author_name
    b.save()
    return redirect("blog")


def search(request):
    if request.method == 'POST':
        q = request.POST['q']
        blogs = Blog.objects.filter(blog_title__icontains=q)
        return render(request, 'search.html', {'q': q, 'blogs': blogs})
    else:
        return render(request, 'search.html', {})
