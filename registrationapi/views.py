from django.shortcuts import render
from . models import User
from registrationapi.serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import re
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.
def SignupPage(request):
    return render(request,'register/Signup.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email= request.POST['email']
        password = request.POST['password']
        full_name = request.POST['full_name']
        age = request.POST['age']
        gender = request.POST['gender']

        new_user = User.objects.create(username=username, email=email, password=password,full_name=full_name,age=age,gender=gender)
        message = "User Registered successfully"
        return render(request,'register/home.html', {'msg':message})



class UserViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def validate_password(self, password):
        # Password must be at least 8 characters long and contain a mix of uppercase and lowercase letters,
        # numbers, and special characters.
        regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
        return regex.match(password)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            age = serializer.validated_data['age']
            gender = serializer.validated_data['gender']

            # Check if a user with the given username already exists
            if User.objects.filter(username=username).exists():
                response_data = {
                    "status": "error",
                    "code": "USER_NAME_EXISTS",
                    "message": "The provided username is already taken. Please choose a different username."
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            # Check if a user with the given email already exists
            if User.objects.filter(email=email).exists():
                response_data = {
                    "status": "error",
                    "code": "EMAIL_EXISTS",
                    "message": "The provided email is already associated with an existing user."
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            # Check if the provided password meets the requirements
            if not self.validate_password(password):
                response_data = {
                    "status": "error",
                    "code": "INVALID_PASSWORD",
                    "message": "The provided password does not meet the requirements. Password must be at least 8 characters long and contain a mix of uppercase and lowercase letters, numbers, and special characters."
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            # Check if the age is a positive integer
            if not isinstance(age, int) or age <= 0:
                response_data = {
                    "status": "error",
                    "code": "INVALID_AGE",
                    "message": "Age must be a positive integer."
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            # Check if the gender field is required and has a valid value
            valid_genders = ["male", "female", "non-binary"]
            if gender not in valid_genders:
                response_data = {
                    "status": "error",
                    "code": "INVALID_GENDER",
                    "message": "Gender field is required. Please specify the gender (e.g., male, female, non-binary)."
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            

            serializer.save()

            response_data = {
                "status": "success",
                "message": "User successfully registered!",
                "data": serializer.data
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        response_data = {
            "status": "error",
            "code": "INVALID_REQUEST",
            "message": "Invalid request. Please provide all required fields: username, email, password, full_name."
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    

    def update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "status": "success",
                "message": "Data Updated successfully",
                "data": serializer.data
            }
            return Response(response_data)
        response_data = {
            "status": "error",
            "code": "KEY_ERROR",
            "message": "Invalid User"
        }
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        response_data = {
                "status": "success",
                "message": "Data Deleted successfully",
            }
        return Response(response_data,status=204)
  