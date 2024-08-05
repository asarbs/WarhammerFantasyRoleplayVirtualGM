from rest_framework import serializers

from cms.models import News

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'lead', 'contents', 'is_yt', 'internal_id']