from rest_framework import viewsets

from rest_framework.decorators import action

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from rest_framework.permissions import DjangoModelPermissions

from rest_framework.filters import SearchFilter

from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from news.models import NewsPost

from api.v1.news.subserializers.news import NewsPostSerializer


class NewsPostViewSet(viewsets.ModelViewSet):

    queryset = NewsPost.objects.all()
    lookup_field = 'slug'
    serializer_class = NewsPostSerializer

    permission_classes = [
        AllowAny
    ]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created', 'rate',]
    search_fields = ['title',]

    @action(detail = False, methods = ['get'])
    def newest(self, request, pk = None):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest, context={'request': request})
        return Response(serializer.data)

    @action(detail = False, methods = ['get'])
    def latest(self, request, pk = None):
        latest = self.get_queryset().order_by('created')[:3]
        serializer = self.get_serializer_class()(latest, context={'request': request})
        return Response(serializer.data)

    @action(detail = False, methods = ['get'])
    def important_posts(self, request, pk = None):
        important_posts = self.get_queryset().filter(important = True).order_by('created')
        serializer = self.get_serializer_class()(important_posts, context={'request': request})
        return Response(serializer.data)

    @action(detail = False, methods = ['get'])
    def oldest(self, request, pk = None):
        oldest = self.get_queryset().order_by('created').first()
        serializer = self.get_serializer_class()(oldest, context={'request': request})
        return Response(serializer.data)
