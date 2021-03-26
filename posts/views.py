from rest_framework import generics, viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from posts.models import Comment, MyUser, Post
from posts.seializers import CommentSerializer, UserSerializer, PostSerializer


class UserViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class PostViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

