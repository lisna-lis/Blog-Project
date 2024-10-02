from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer
from .serializers import TagsSerializer

from .models import Blog
from .models import Tags
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

## Custom pagination ##
class CustomPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100

# Create your views here.
class BlogCreateView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']
    serializer_class = BlogSerializer
    def post(self,request):
        user = request.user
        tags = request.data.get('tags',None)
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            blog = serializer.save(user=user)
            if tags:
                tags = json.loads(tags)
                blog.tags.add(*tags)
            return Response({"msg":"Blog Created Successfully"},status=201)
        else:
            return Response(serializer.errors,status=400)



class BlogRetreiveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get','put','delete']
    serializer_class = BlogSerializer 
    def get_obj(self,request,uuid):
        user = request.user
        try :
           blog = Blog.objects.get(user=user,uuid=uuid)
        except Blog.DoesNotExist:
            blog = Blog.objects.none()
        return blog    
    

    def get(self,request,uuid):
        blog = self.get_obj(request,uuid)
        serializer = self.serializer_class(blog)
        return Response(serializer.data,status=200)

    def put(self,request,uuid):
        data = request.data
        blog = self.get_obj(request,uuid)
        serializer = self.serializer_class(blog,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Blog Updated"},status=200)
        else:
            return Response(serializer.errors,status=400)

    def delete(self,request,uuid):
        blog = self.get_obj(request,uuid)
        blog.active_status=False
        blog.save()
        return Response({"msg":"Blog Deleted Successfully"},status=200)
    

class PublicBlogListView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    http_method_names = ['get']
    serializer_class = BlogSerializer
    def get(self,request):
        blogs = Blog.objects.filter()
        print(blogs)
        serializer = self.serializer_class(blogs,many=True)
        return Response(serializer.data,status=200)
    

class PublicBlogRetreiveView(APIView):
    http_method_names = ['get']
    serializer_class = BlogSerializer
    def get_obj(self,uuid):
        try :
           blog = Blog.objects.get(uuid=uuid)
        except Blog.DoesNotExist:
            blog = Blog.objects.none()
        return blog 
    def get(self,request,uuid):
        blog = self.get_obj(uuid)
        serializer = self.serializer_class(blog)
        return Response(serializer.data,status=200)
    

class UserBlogListView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    http_method_names = ['get']
    serializer_class = BlogSerializer
    def get(self,request):
        user = request.user
        blogs = Blog.objects.filter(active_status = True, user = user)
        serializer = self.serializer_class(blogs,many=True)
        return Response(serializer.data,status=200)

    



