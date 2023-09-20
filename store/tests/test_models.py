from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='book', slug='book')

    def test_category_model_entry(self):
        """

        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """

        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertEqual(str(data), 'book')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='book', slug='book')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='my book', created_by_id=1, slug='my-book', price='90', image='book')

    def test_products_model_entry(self):
        """

        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertEqual(str(data), 'book')
