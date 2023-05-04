from django.test import TestCase
from shop.models import Product, Category
from django.utils import timezone
from mainapp.models import CustomUser

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(
            name = 'Fashion',
            slug = 'fashion',
            created_at = timezone.now(),
            updated_at = timezone.now()
        )

    def test_model(self):
        cat = Category.objects.get(id=1)
        self.assertEqual(cat.name, 'Fashion')

class ProductTestCase(TestCase):
    def setUp(self):
        
        self.user = CustomUser.objects.create(email='test@email.com', first_name='test', last_name='user', password='')
        self.user.set_password('secret')
        self.user.save()       
        Category.objects.create(name='Fashion', slug='fashion', created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(
            owner=self.user,
            category=Category.objects.get(id=1),
            name='Hat', slug='hat',description='Amazing hat',
            price=49.99, available=True, 
            created_at=timezone.now(), updated_at=timezone.now(), 
            image=None
        )

    def test_contact_model(self):
        item = Product.objects.get(id=1)
        self.assertEqual(item.name, 'Hat')