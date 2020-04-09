from django.shortcuts import render, get_object_or_404
from .models import Blogs
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def blogs(request):
    blogs = Blogs.objects.order_by('-blog_date')
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    page_blogs = paginator.get_page(page)
    context = {
        'blogs':page_blogs
    }
    return render(request,'blogs/blog.html', context)

def blog(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    context = {
        'blog':blog
    }
    return render(request, 'blogs/singleblog.html', context)     
