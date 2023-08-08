from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = URL
        fields = ['pk', 'long_url', 'short_code']