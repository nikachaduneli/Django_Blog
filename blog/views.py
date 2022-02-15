from django.shortcuts import render, redirect
from django.contrib.auth.mixins import(  
  LoginRequiredMixin,
  UserPassesTestMixin
  )
from .models import Post
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView, 
  UpdateView,
  DeleteView
  )
from .forms import CommentForm  
from django.contrib import messages


class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by=5
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    users = User.objects.all().order_by('date_joined').reverse()
    context['users'] = users
    context['title'] = 'Home'
    return context

class PostDetailViev(LoginRequiredMixin, DetailView):
  model = Post
  form = CommentForm

  def post(self, request, *args, **kwargs):
    form = CommentForm(request.POST)
    if form.is_valid():
      post = self.get_object()
      form.instance.author = request.user
      form.instance.post = post
      form.save()
      return redirect('post_detail',pk=post.id)

  def get_context_data(self, **kwargs):
    context =  super().get_context_data(**kwargs)
    context['title'] = self.object.title
    context['form'] = self.form
    return context

class PostCreateView(LoginRequiredMixin ,CreateView):
  model = Post
  fields = ['title', 'content']
  template_name = 'blog/post_create.html'

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

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = f'Update {self.object.title}'
    return context 

class PostDeleteiew(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  template_name = 'blog/post_delete.html'
  success_url = '/'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = f'Delete {self.object.title}'
    return context

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False 

def about(request):
  return render(request,"blog/about.html",{'title':'about'})   

def error500(request):
  return render(request,'blog/error500.html')

def error404(request,exception):
  return render(request, 'blog/error404.html')

def error403(request,exception):
  return render(request,'blog/error403.html')