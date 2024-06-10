from rest_framework import serializers
from .models import customUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password




class Userserializer(serializers.ModelSerializer):
	UserName=serializers.CharField()
	password=serializers.CharField(write_only=True)
	class Meta:
		model=customUser
		fields=('Email','password','UserName')
	def create(self, data):
		print(data)
		user =customUser.objects.create_user(email=data['Email'],password=data['password'],username=data['UserName'])
		return user 

class LoginSerializer(TokenObtainPairSerializer):
	@classmethod
	def get_token(cls, user):
		print("user: ", user)
		token=super().get_token(user)

		return token

	def validate(self,attrs):
		print("attribute: ",attrs)
		#print("validateattribute: ",super().validate(attrs))
		#print(attrs[self.username_field])
		#print(attrs["password"])
		user=super().validate(attrs)
		#user = authenticate(username=attr['Email'], password=attr['password'])
		print("validate: ",user)
		user.update({"email":self.user.Email})
		return user

	