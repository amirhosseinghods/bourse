from django.contrib.auth.models import User

from rest_framework import serializers

from analysis.models import AnalyzePost


class AnalyzeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AnalyzePost
        fields = ('url', 'title', 'slug', 'summary', 'content', 'important', 'is_shown', 'height_field', 'width_field', 'picture', 'category',)