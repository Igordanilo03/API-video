from rest_framework import serializers
from video.models import Video, Category


class VideoModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url', 'category']
        
    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        if 'category' not in ret or ret['category'] is None:
            try:
                ret['category'] = Category.objects.get(id=1)
            except Category.DoesNotExist:
                raise serializers.ValidationError("Categoria padrão não encontrada.")
        return ret

    def create(self, validated_data):
        return Video.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'category' not in validated_data or validated_data['category'] is None:
            validated_data['category'] = Category.objects.get(id=1)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
        

class CategoryModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'title', 'color']
        
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("O campo é obrigatório")
        return value
    
    def validate_color(self, value):
        if not value:
            raise serializers.ValidationError("O campo é obrigatório")
        return value