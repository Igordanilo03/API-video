import re
from rest_framework import serializers
from video.models import Category

def validate_non_empty(value, field_name):
    """Valida se um campo não está vazio."""
    if not value:
        raise serializers.ValidationError(f"O campo {field_name} é obrigatório.")
    return value

def validate_color(value):
    """Valida se uma cor é um código hexadecimal válido."""
    value = validate_non_empty(value, "cor")
    if not re.match(r'^#[0-9A-Fa-f]{6}$', value):
        raise serializers.ValidationError("A cor deve ser um código hexadecimal válido (ex.: #FF0000).")
    return value

def get_default_category():
    """Retorna a categoria padrão ou levanta erro se não existir."""
    try:
        return Category.objects.get(id=1)  
    except Category.DoesNotExist:
        raise serializers.ValidationError("Categoria padrão não encontrada.")