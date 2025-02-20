from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from video.models import Video, Category
from video.serializers import VideoModelSerializer, CategoryModelSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class VideoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoModelSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title']
    search_fields = ['title']
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class VideoRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoModelSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class CategoryRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class VideosByCategoryListAPIView(generics.ListAPIView):
    serializer_class = VideoModelSerializer
    
    def get_queryset(self):
        category_id = self.kwargs['id']
        return Video.objects.filter(category_id=category_id)