from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="A sample product for testing",
            price=100.00
        )
    
    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "A sample product for testing")
        self.assertEqual(self.product.price, 100.00)

class ProductListViewTest(TestCase):
    def test_product_list_view(self):
        response = self.client.get(reverse('crudapp:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crudapp/product_list.html')

class ProductCreateViewTest(TestCase):
    def test_product_create_view(self):
        response = self.client.get(reverse('crudapp:product_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crudapp/product_form.html')

class ProductDeleteViewTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="A sample product for testing",
            price=100.00
        )
        self.delete_url = reverse('crudapp:product_delete', kwargs={'pk': self.product.pk})
    
    def test_product_delete_view(self):
        # Check that the product exists before deletion
        self.assertEqual(Product.objects.count(), 1)

        # Perform the delete operation
        response = self.client.post(self.delete_url)

        # Verify the response and that the product was deleted
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after deletion
        self.assertEqual(Product.objects.count(), 0)

        # Optional: Test if the redirect goes to the expected URL
        self.assertRedirects(response, reverse('crudapp:product_list'))