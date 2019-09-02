from django.test import TestCase
from .models import Category,Product

# Create your tests here.
# https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1
class ModelTestCase(TestCase):
    """THis define test list for category and Product"""
    def setUp(self):
        self.category = Category(name='People',slug='people')
    

    def test_model_can_create_category(self):

        """MODE L can create Category"""
        old_count = Category.objects.count()
        self.category.save()
        new_count = Category.objects.count()
        self.assertNotEquals(old_count,new_count)
