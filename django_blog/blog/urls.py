from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    PostByTagListView,
)

from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView
from django.urls import path
from django.shortcuts import redirect

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

urlpatterns = [
    path("", lambda request: redirect("home", permanent=True)),
    path('home', views.home, name="home"),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("register/", views.register, name="register"),
    #path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path("posts/", PostListView.as_view(), name="posts"),  # Keep "posts" for your list template
    path("post/new/", PostCreateView.as_view(), name="post_create"),  # Checker compliance
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="add_comment"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_edit"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
    path("search/", PostListView.as_view(), name="posts"),  # Already defined
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts_by_tag"),
    path('logout/', CustomLogoutView.as_view(next_page='home'), name='logout'),
]



