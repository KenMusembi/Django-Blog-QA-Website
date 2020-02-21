from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
from django.http import HttpResponse

def home(request):
    context = {
            'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


def about(request):
    #return HttpResponse("<h1>Blog aboutpage</h1>")
    return render(request, 'blog/about.html', {'title': 'About'})