from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include("blog.urls")),
    path('admin/', admin.site.urls),

    path('register/', user_views.register, name='user_register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='user_logout'),

    path('profile/', user_views.profile, name='user_profile'),
    path('detail_profile/<int:pk>', user_views.UserDetailView.as_view(template_name='users/detail_profile.html'),
         name='detail_profile'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'),
         name='password_reset'),

    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'blog.views.error404'
handler500 = 'blog.views.error500'
handler403 = 'blog.views.error403'
