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

from blog.models import Tag
from ..subserializers.tags import TagSerializer

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly,
        DjangoModelPermissions,
    ]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created']
    search_fields = ['title',]

    @action(detail=True, methods = ['get'])
    def posts(self, request, pk = None):
        tag = self.get_object()
        serializer = TagSerializer(tag.posts.all(), many = True)
        return Response(serializer.data)