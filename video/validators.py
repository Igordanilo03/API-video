import re
from rest_framework import serializers
from video.models import Category


def validate_non_empty(value, field_name):
    if not value:
        raise serializers.ValidationError(f"O campo {field_name} é obrigatório.")
    return value


def validate_color(value):
    value = validate_non_empty(value, "cor")
    if not re.match(r'^#[0-9A-Fa-f]{6}$', value):
        raise serializers.ValidationError("A cor deve ser um código hexadecimal válido (ex.: #FF0000).")
    return value


def get_default_category():
    try:
        return Category.objects.get(id=1)  
    except Category.DoesNotExist:
        raise serializers.ValidationError("Categoria padrão não encontrada.")