from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotFound
from video.models import Video, Category
from video.serializers import VideoModelSerializer, CategoryModelSerializer


class BaseVideoAPIView(generics.GenericAPIView):
    queryset = Video.objects.select_related('category')  
    serializer_class = VideoModelSerializer
    authentication_classes = [BasicAuthentication] 
    permission_classes = [IsAuthenticatedOrReadOnly]  


class VideoListCreateAPIView(BaseVideoAPIView, generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category']  
    ordering_fields = ['title', 'category__title']  
    search_fields = ['title', 'description']  


class VideoRetrieveUpdateDestroyAPIView(BaseVideoAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]  


class BaseCategoryAPIView(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryListCreateAPIView(BaseCategoryAPIView, generics.ListCreateAPIView):
    ordering_fields = ['title']  
    search_fields = ['title']  


class CategoryRetrieveUpdateDestroyAPIView(BaseCategoryAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]  


class VideosByCategoryListAPIView(BaseVideoAPIView, generics.ListAPIView):
    def get_queryset(self):
        category_id = self.kwargs['id']  
        if not Category.objects.filter(id=category_id).exists():
            raise NotFound("Categoria não encontrada.")  
        return Video.objects.filter(category_id=category_id).select_related('category')