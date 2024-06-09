from rest_framework import serializers

from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    '''
    Serializers для модели объявления.
    '''
    class Meta:
        model = Advertisement
        fields = ['title', 'ad_id', 'author', 'views', 'position']
