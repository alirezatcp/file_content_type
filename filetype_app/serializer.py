from rest_framework import serializers

from django.utils import timezone


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
    time = serializers.DateTimeField(default=timezone.now())
