from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        extra_kwargs = {
            "slug": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }