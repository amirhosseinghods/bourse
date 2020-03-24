from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import PrimaryKeyRelatedField
from rest_framework.serializers import StringRelatedField

from django.contrib.auth.models import User
from blog.models import Post
from blog.models import Tag

from ..subserializers.tags import TagSerializer

class PostSerializer(HyperlinkedModelSerializer):
    tags = PrimaryKeyRelatedField(many=True, queryset = Tag.objects.all(), write_only = True)
    tag_display = StringRelatedField(source = 'tags')
    author = PrimaryKeyRelatedField(many=False, queryset = User.objects.all())

    class Meta:
        model = Post
        fields = ('url', 'title', 'summary', 'picture', 'category', 'author', 'tags', 'tag_display')