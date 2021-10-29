from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'content', 'created_at', 'updated_at', 'count_of_likes']


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['url', 'user', 'content', 'created_at', 'updated_at', 'count_of_likes']

    def get_url(self, obj):
        return obj.get_api_url()

class PostDetailSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ["id", "slug",'user', 'content', 'created_at', 'updated_at', 'count_of_likes']

    def get_slug(self, obj):
        return obj.slug