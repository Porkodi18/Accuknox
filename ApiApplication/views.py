from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import Userserializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import customUser
from django.db.models import Q
# Create your views here.

class SignUp(APIView):
	def post(self, request):
		register=Userserializer(data=request.data)
		if register.is_valid():
			saved_value=register.save()
			print("saved:",saved_value)
			regist_dict={'email':saved_value.Email,'user_Name':saved_value.UserName}
			return Response(regist_dict,status=status.HTTP_201_CREATED)

		return Response(register.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(TokenObtainPairView):
	serializer_class=LoginSerializer

class SearchView(APIView):
	permission_classes=[IsAuthenticated]
	def get(self,request):
		query=request.query_params.get('search','')
		user=customUser.objects.filter(Q(UserName__icontains=query) | 
            Q(Email__icontains=query))
		serializers=Userserializer(user,many=True)
		return Response(serializers.data, status=status.HTTP_200_OK)









