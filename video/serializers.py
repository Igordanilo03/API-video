from rest_framework import serializers
from video.models import Video, Category
from .validators import validate_non_empty, validate_color, get_default_category

class VideoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url', 'category']

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        if 'category' not in ret or ret['category'] is None:
            ret['category'] = get_default_category()
        return ret

    def update(self, instance, validated_data):
        if 'category' not in validated_data or validated_data['category'] is None:
            validated_data['category'] = get_default_category()
        instance.__dict__.update(validated_data)
        instance.save()
        return instance

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'color']

    def validate_title(self, value):
        return validate_non_empty(value, "título")

    def validate_color(self, value):
        return validate_color(value)