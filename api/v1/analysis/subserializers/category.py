from django.contrib.auth.models import User

from rest_framework import serializers

from analysis.models import AnalyzeCategory


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AnalyzeCategory
        fields = ('url', 'title', 'slug',)
