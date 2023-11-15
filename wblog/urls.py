from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('new_post/', views.NewPost.as_view(), name='new_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        'about',
        views.generic.TemplateView.as_view(template_name='about.html'),
        name='about'),
]
