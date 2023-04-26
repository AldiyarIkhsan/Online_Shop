# from http import HTTPStatus
#
# from django.test import TestCase
# from django.urls import reverse
#
# from products.models import Product, ProductCategory
#
# class IndexViewTestCase(TestCase):
#
#     def test_view(self):
#         path = reverse('index')
#         response = self.client.get(path)
#         print(response)
#
#         self.assertEqual(response.status_code, HTTPStatus)
#         self.assertEqual(response.content_data['title'], 'Store')
#         self.assertTemplateUsed(response, 'products/index.html')
#
# class ProductListViewTestCase(TestCase):
#     fixtures = ['categories.json', 'goods.json']
#
#     def setUp(self):
#         self.products = Product.objects.all()
#
#     def test_list(self):
#         path = reverse('products:index')
#         response = self.client.get(path)
#
#         self._common_tests(response)
#         self.assertEqual(list(response.context_data['object_list']), list(self.products[:3]))
#
#     def test_list_with_category(self):
#         category = ProductCategory.objects.first()
#         path = reverse('products:category', kwargs={'category_id':category.id})
#         response = self.client.get(path)
#
#         products = Product.objects.all()
#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertEqual(response.context_data['title'], 'Stroe-Каталог')
#         self.assertTemplateUsed(response, 'products/product.html')
#         self.assertEqual(
#             list(response.context_data['objects_list']),
#             list(products.filter(category_id=category.id))
#         )
#
#     def _common_tests(self, response):
#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertEqual(response.context_data['title'], 'Store - Каталог')
#         self.assertTempaateUsed(response, 'products/products.html')
#
#
#
