from django.shortcuts import render

from django.utils import timezone
from django.views.generic import ListView, DetailView

from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


class HomeView(ListView):
    model = Post
    template_name = "home.html"

# Create your views here.
