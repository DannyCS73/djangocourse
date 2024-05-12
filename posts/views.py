from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView, permission_classes
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .permissions import ReadOnly, AuthorOrReadOnly


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def homepage(request:Request):

    if request.method == "POST":
        data = request.data
        response = {"message": "Hello World!", "data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {"message": "Hello World!"}
    return Response(data=response, status=status.HTTP_200_OK)

# class PostViewset(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PostSerializer
    permission_classes = [ReadOnly]
    queryset = Post.objects.all()

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.save(author=user)
    #     return super().perform_create(serializer)

    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AuthorOrReadOnly]

    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class PostListCreateView(APIView):
#     serializer_class = PostSerializer

#     def get(self, request:Request, *args, **kwargs):
#         posts= Post.objects.all()
#         serializer = self.serializer_class(instance=posts, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def post(self, request:Request, *args, **kwargs):
#         data = request.data
#         serializer = self.serializer_class(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message" : "Post Created.",
#                 "data" : serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostRetrieveUpdateDeleteView(APIView):
#     serializer_class = PostSerializer

#     def get(self, request:Request, post_id:int):
#         post = get_object_or_404(Post, pk=post_id)
#         serializer = self.serializer_class(instance=post)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def put(self, request:Request, post_id:int):
#         post = get_object_or_404(Post, pk=post_id)
#         data = request.data
#         serializer = self.serializer_class(instance=post, data=data)

#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message" : "Post Updated.",
#                 "data": serializer.data
#             }
#             return Response(data=response, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request:Request, post_id:int):
#         post = get_object_or_404(Post, pk=post_id)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



