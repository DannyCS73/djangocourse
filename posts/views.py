from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

posts = [
    {
        "id": 1,
        "title": "Why is it difficult to learn Programming?",
        "content": "This is to give reasons why its hard."
    },
    {
        "id": 2,
        "title": "Learn JavaScript.",
        "content": "This is a course on JavaScript."
    },
    {
        "id": 3,
        "title": "Why is it difficult to learn Programming?",
        "content": "This is to give reasons why its hard."
    }
]

@api_view(http_method_names=["GET", "POST"])
def homepage(request:Request):

    if request.method == "POST":
        data = request.data
        response = {"message": "Hello World!", "data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {"message": "Hello World!"}
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def list_posts(request:Request):
    return Response(data=posts, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail_view(request: Request, post_index:int):
    post = posts[post_index-1]
    if post:
        return Response(data=post, status=status.HTTP_200_OK)

    return Response(data={"Error":"post not found"}, status=status.HTTP_404_NOT_FOUND)
