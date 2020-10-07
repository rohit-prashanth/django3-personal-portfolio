from django.shortcuts import render, get_object_or_404
from .models import Project_blog

def all_blogs(request):
    project_blog = Project_blog.objects.order_by('-time')[:5]
    return render(request, 'blog/all_blogs.html',{'project_blog':project_blog})


def detail(request, blog_id):
    blogs = get_object_or_404(Project_blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blogs' : blogs})
