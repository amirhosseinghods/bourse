from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from django_filters.rest_framework import DjangoFilterBackend
from painless.api_permissions import IsStaffModifier

from blog.models import Post
from ..subserializers.post import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly,
        # IsStaffModifier,
        DjangoModelPermissions,
    ]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created']
    filter_fields = ['category', 'author']
    search_fields = ['title', 'author']

    # @action(detail=True, methods = ['get'])
    # def tags(self, request, pk = None):
    #     post = self.get_object()
    #     serializer = PostSerializer(post.tags.all(), many = True)
    #     return Response(serializer.data)