from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
	


# Create your models here.

class Usermanager(BaseUserManager):
	def create_user(self, email, password, username):
		user=self.model(Email=email,UserName=username)
		print("password:",password)
		user.set_password(password)
		user.save(using=self._db)
		return user


class customUser(AbstractBaseUser):
	Email=models.EmailField(unique=True)
	UserName=models.CharField(max_length=15)
	objects=Usermanager()
	USERNAME_FIELD="Email"
	def __str__(self):
		return self.Email
