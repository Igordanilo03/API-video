from django.urls import path
from .views import (
    VideoListCreateAPIView, VideoRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView,
    VideosByCategoryListAPIView
)

urlpatterns = [
    path('videos/', VideoListCreateAPIView.as_view(), name='video-list-create'),
    path('videos/<int:pk>/', VideoRetrieveUpdateDestroyAPIView.as_view(), name='video-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('categories/<int:id>/videos/', VideosByCategoryListAPIView.as_view(), name='videos-by-category'),
]