from django import test
from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTest(TestCase) :
  """Testing user Model"""
  def test_can_create_a_user(self):
    """create user with userName , email , password"""
    username = 'merhan'
    email = 'mehran@mehran.com'
    password = '1231456'
    user = get_user_model().objects.create_user(
      username = username,
      email=email,
      password=password,
    )

    self.assertEqual(user.email , email)

    self.assertTrue(user.check_password(password))
