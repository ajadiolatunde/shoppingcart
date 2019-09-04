from django.test import TestCase
from .models import Category,Product
from django.urls import reverse
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

# Create your tests here.
# https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1

# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
class ModelTestCase(TestCase):
    """THis define test list for category and Product"""
    def setUp(self):
        self.category = Category(name='People',slug='people')

        self.client = APIClient()
        self.category_data = {'name': 'Computer','slug': 'computer'}
        # self.response = self.client.post(reverse('create'),self.category_data,format="json")

        self.user = User(username='olatunde',password='dannynoc')


    def test_user_can_login(self):
        self.user.set_password('dannynoc')
        self.user.save()
        user = authenticate(username='olatunde',password='dannynoc')
        token = Token.objects.create(user=self.user)
        print ("Tunde -----",token)


        self.assertNotEquals(user,None,"Cant login")


    def test_api_can_login(self):
        self.credentials = {
            'username': 'olatunde',
            'password': 'dannynoc'}

        print ("Tunde -----",self.credentials)
        response = self.client.post(reverse('shop:login'), self.credentials, follow=True)
        print (response.json())
        self.assertTrue(response.context['user'].is_active)


    def test_model_can_create_category(self):

        """MODE L can create Category"""
        old_count = Category.objects.count()
        self.category.save()
        new_count = Category.objects.count()
        self.assertNotEquals(old_count,new_count)

    def test_api_can_create_a_Category(self):
        """Test the api has bucket creation capability."""
        # self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
