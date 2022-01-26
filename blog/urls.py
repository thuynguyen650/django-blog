from django.urls import path
from . import views
from .views import HomeListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserHomeListView, CategoryListView

urlpatterns = [
    path('', HomeListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserHomeListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    path('category/<str:category>/', CategoryListView.as_view(), name='category-posts'),

    path('about/', views.about, name='blog-about'),
]