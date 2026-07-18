from rest_framework.serializers import ModelSerializer
from app.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'name', 'email','subject', 'message']
