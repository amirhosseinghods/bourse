from django.contrib.auth.models import User

from rest_framework import serializers

from news.models import NewsPost


class NewsPostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = NewsPost
        fields = ('url', 'title', 'slug', 'summary', 'content', 'important', 'is_shown', 'height_field', 'width_field', 'picture', 'category',)
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }