from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer, PostListSerializer, PostDetailSerializer

class CreatePostAPIView(APIView):
    """
    post:
        Creates a new post instance. Returns created post data

        parameters: [content]
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)

class ListPostAPIView(ListAPIView):
    """
    get:
        Returns a list of all existing posts
    """

    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DetailPostAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the details of a post instance. Searches post using slug field.

    put:
        Updates an existing post. Returns updated post data

        parameters: [slug, title, body, description, image]

    delete:
        Delete an existing post

        parameters = [slug]
    """

    queryset = Post.objects.all()
    lookup_field = "slug"
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class PostLikeAPIView(APIView):
    """
    post:
        Like a Post instance.

        parameters: [slug]

    """
    permission_classes = [IsAuthenticated]

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        post.count_of_likes = post.count_of_likes + 1
        post.save()
        return Response({"Done !"}, status=200)
