from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import PrimaryKeyRelatedField

from blog.models import Tag

class TagSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = Tag
        fields = ('url', 'title',)