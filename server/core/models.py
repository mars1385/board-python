from django.db import models

from django.contrib.auth.models import BaseUserManager ,AbstractBaseUser,PermissionsMixin
# Create your models here.

class UserManger(BaseUserManager):

  def create_user(self , username,email , password):
    """create and save user """
    user = self.model(email=email , username = username )

    user.set_password(password)

    user.save(using=self._db)

    return user
  

class User(AbstractBaseUser , PermissionsMixin):
  """ User Model """
  username = models.CharField(max_length=255)
  email = models.EmailField(max_length=255 , unique=True)

  objects = UserManger()

  USERNAME_FIELD = 'email'

