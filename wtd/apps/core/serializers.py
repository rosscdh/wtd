# -*- coding: UTF-8 -*-
from rest_framework import serializers

from .models import Page


class DiffSerializer(serializers.Serializer):
    diff = serializers.CharField()


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page