from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator


# def decorate(func):
#     def inner(request):
#         if request.user.is_authenticated:
#             print(f"{request.user.username} user.")
#             return func(request)
#         else:
#             return redirect('/account/login/')
#     return inner

# @decorate
def home(request):
    if request.GET.get('category'):
        posts = Post.objects.filter(category_id=request.GET.get('category'))
        if not posts:
            posts = []
            post = []
        else:
            post = posts[0]
    else:
        posts = Post.objects.all()
        post = posts[0]
    paginator = Paginator(posts, 4)

    if request.GET.get('page'):
        page_number = request.GET.get('page')
    else:
        page_number = 1
    post_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    comments = Comment.objects.all()[:5]
    content = {'post': post, 'comments': comments, 'post_obj': post_obj, 'categories': categories}
    return render(request, 'post/home.html', content)


def detail(request, id):
    if request.method == "POST":
        user = request.user
        if user.is_authenticated:
            comment = request.POST['comment']
            Comment.objects.create(user=user, post=Post.objects.get(id=id), text=comment)
        else:
            return redirect('/account/login/')

    if request.GET.get("category"):
        posts = Post.objects.filter(category_id=request.GET.get('category'))
        if not posts:
            posts = []
            post = []
        else:
            post = posts[0]

        paginat = Paginator(posts, 4)

        if request.GET.get('page'):
            page_number = request.GET.get('page')
        else:
            page_number = 1
        post_obj = paginat.get_page(page_number)
        categories = Category.objects.all()
        comments = Comment.objects.all()[:5]

        content = {'post': post, 'post_obj': post_obj, 'categories': categories, 'comments': comments}
        return render(request, 'post/home.html', content)

    post = Post.objects.get(id=id)
    post.see_add()
    post.save()
    categories = Category.objects.all()
    comments = Comment.objects.filter(post=post)
    content = {'post': post, 'categories': categories, 'comments': comments}
    return render(request, 'post/detail.html', content)


def about(request):
    return render(request, 'post/about.html')


def contact(request):
    return render(request, 'post/contact.html')
