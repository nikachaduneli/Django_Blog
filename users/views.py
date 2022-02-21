from django.shortcuts import( 
  render, 
  redirect, 
  get_object_or_404
  )
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from .forms import (
  UserRegisterForm, 
  ProfileUpdateForm, 
  UserUpdateForm)
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.core.paginator import( 
  Paginator, 
  InvalidPage
  )

def register(request):

  if request.method == 'POST':

    form = UserRegisterForm(request.POST)
    
    if form.is_valid():
      #check if email is already in use
      email = form.cleaned_data.get('email')
      email = User.objects.filter(email=email).first()
      
      if email:
        messages.warning(request, 'This email Is Already In Use By Another User.')
        return redirect('user_register')

      username = form.cleaned_data.get('username')
      messages.success(request, f'{username} Account Has Been created')
      form.save()
      return redirect('user_login')
  
  else:
    form = UserRegisterForm()
  
  context = {
    'form':form,
    'title':'Registration'
    }

  return render(request, 'users/register.html',context=context )

@login_required(login_url='user_login')
def profile(request):

  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, 
                               request.FILES, 
                               instance=request.user.profile)
    
    if u_form.is_valid and p_form.is_valid:
      u_form.save()
      p_form.save()
      messages.success(request, 'Your Profile Has Been Updated.')
      return redirect('user_profile')                           
  
  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
  
  ##pagination here
  posts = Post.objects.filter(author=request.user).order_by('date_posted').reverse()
  posts_per_page = 5
  is_paginated = False

  if len(posts) > posts_per_page:
    page = request.GET.get('page',1)
    paginator = Paginator(posts,posts_per_page)
    page_obj = paginator.get_page(page)
    try:
      posts = paginator.page(page)
    except InvalidPage:
      posts = paginator.page(1)  
    is_paginated = True  
  
  context={
    'u_form':u_form,
    'p_form':p_form,
    'title':f'{request.user.username}\'s Profile',
    'search':True,
  }
  
  if is_paginated:
    context['posts']=posts
    context['page_obj'] = page_obj
    context['is_paginated'] = is_paginated
  
  return render(request, 'users/profile.html', context=context)

class UserDetailView(ListView):

  model = Post
  template_name='blog/detail_profile.html'
  context_object_name = 'posts'
  paginate_by = 5

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = get_object_or_404(User, id=self.kwargs.get('pk'))
    context['title'] = f'{user}s\' Profile'
    context['user'] = user
    context['search'] = True
    return context

  def get_queryset(self):
    user = get_object_or_404(User, id=self.kwargs.get('pk')) 
    return Post.objects.filter(author=user).order_by('date_posted').reverse()    