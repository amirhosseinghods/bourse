from django.contrib.auth.models import User

from rest_framework import serializers

from news.models import NewsCategory


class NewsCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = NewsCategory
        fields = ('url', 'title', 'slug',)
