import os
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("ADMINS")

class PostAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        text = (
            f"📩 Yangi murojaat\n\n"
            f"👤 Ism: {post.name}\n"
            f"📧 Email: {post.email}\n"
            f"📝 Mavzu: {post.subject}\n"
            f"💬 Xabar:\n{post.message}"
        )
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": CHAT_ID,
                "text": text
            }
        )
        return Response({"message": "Message sent successfully"}, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
