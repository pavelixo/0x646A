from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer


class ArticlePagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100  


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"

    pagination_class = ArticlePagination
    filter_backends = [SearchFilter]
    search_fields = ["title"]
