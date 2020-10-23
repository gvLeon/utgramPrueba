""" utgram URLs """
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Static files config
from django.conf import settings
from django.conf.urls.static import static

# importando las vistas
from django.contrib.auth import views as auth_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    

    # PostViews
    path('', posts_views.list_post,name='feed'),
    path('new/',posts_views.create_post, name='create_post'),

    # Users views
    path('login/', users_views.login_view, name='login'),
    path('logout/', users_views.logout_view, name='logout'),
    path('signup/', users_views.signup, name='signup'),
    path('me/profile', users_views.update_profile, name="update_profile"),

    # Restore password views
    path('password_change/',
    auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
    name='password_change' ),

    path('password_change/done/',
    auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
    name='password_change_done' ),


    path('password_reset/',
    auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
    name='password_reset' ),

    path('password_reset/done',
    auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
    name='password_reset_done' ),


    path('reset/<uidb64>/<token>',
    auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
    name='password_reset_confirm'),

    path('reset/complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name='password_reset_complete')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
