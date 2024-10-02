from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Serializer import
from users.serializers import ProfileSerializer
# importing authenticate,refresh token
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import logout as django_logout

from rest_framework.permissions import IsAuthenticated



# Create your views here.

#Register View

class RegisterView(APIView):
    serializer_class = ProfileSerializer
    http_method_names = ['post']
    def post(self,request):
        data = request.data.copy()
        data['username']=data['email']
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"User created Successfully"},status=201)
        else:
            return Response(serializer.errors,status=400)
# Login View        
class LoginView(APIView):
    http_method_names = ['post']
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        
        
        if user is None:
            return Response({"msg": "Invalid Credentials."}, status=400)
        refresh = RefreshToken.for_user(user)
        response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                
            }
        return Response(response_data)
# Updating profile
 
class ProfileRetrieveUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    http_method_names = ['get','put']
    def get(self,request):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data,status=200)
    def put(self,request):
        user = request.user
        data = request.data
        serializer = self.serializer_class(user,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"User Updated Successfully"},status=200)
        else:
            return Response(serializer.errors,status=400)
 
 # Logout View
       
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']
    def post(self, request):
        django_logout(request)
        return Response({"msg":"Logged out successfully"},status=200)

        
