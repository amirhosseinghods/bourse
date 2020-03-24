from rest_framework.serializers import HyperlinkedModelSerializer

from blog.models import Category

class CategorySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('url', 'title',)