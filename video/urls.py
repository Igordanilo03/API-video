from django.urls import path
from . import views

urlpatterns = [
    path('videos/', views.VideoListCreateAPIView.as_view(), name='video-list'),
    path('videos/<int:pk>/', views.VideoRetriveUpdateDestroyAPIView.as_view(), name='video-detail'),
    
    path('categorias/', views.CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categorias/<int:pk>/', views.CategoryRetriveUpdateDestroyAPIView.as_view(), name='category-detail'),
    
    path('categorias/<int:id>/videos/', views.VideosByCategoryListAPIView.as_view(), name='videos-by-category-list')
]