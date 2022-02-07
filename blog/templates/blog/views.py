from turtle import pos
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import  LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView, 
  UpdateView)


def home(request):
  context = {
    'posts':Post.objects.all(),
    'title':'Home'
  }
  return render(request,'blog/home.html', context=context)


class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['posts'] = Post.objects.all().order_by('date_posted').reverse()
      context['title'] = 'Home'
      return context 

class PostDetailViev(DetailView):
  model = Post

class PostCreateView(LoginRequiredMixin ,CreateView):
  model = Post
  fields = ['title', 'content']
  template_name='blog/post_create.html'

  def form_valid(self, form):
    form.instance.author = self.request.user
    
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['title', 'content']
  template_name='blog/post_create.html'

  def form_valid(self, form):
    form.instance.author = self.request.user
    
    return super().form_valid(form)

  def test_func(self):

      post = self.get_object()
      if self.request.user == post.author:
        return True
      return False 

def about(request):
  return render(request,"blog/about.html",{'title':'about'})   