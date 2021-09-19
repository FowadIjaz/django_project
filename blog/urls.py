from django.urls import path
from . import views
# For class based views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
  path('post/<int:pk>/', PostDetailView.as_view(), name = "post-detail"),
  path('post/new/', PostCreateView.as_view(), name = "post-create"),
  path('post/<int:pk>/update/', PostUpdateView.as_view(), name = "post-update"),
  path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = "post-delete"),
  path('user/<str:username>', UserPostListView.as_view(), name = "user-posts"),
  path('', PostListView.as_view(), name = "blog-home"),
  path('about/', views.about, name = "blog-about"),
  path('database/', views.database, name = "database"),
]



# TemplateDoesNotExist at blog/post_list.html
# <app>/<model>_<viewtype>.html