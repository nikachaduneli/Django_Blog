from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="blog_home"),
    path('post/<int:pk>/', views.PostDetailViev.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', views.PostDeleteiew.as_view(), name='post_delete'),
    path('search/', views.PostSearch.as_view(), name='search'),
   
    path('about/', views.about, name='blog_about'),
]

