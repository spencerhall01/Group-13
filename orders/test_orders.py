from django.test import TestCase
from orders.models import Order, OrderItem
from shop.models import Product, Category
from django.utils import timezone
from mainapp.models import CustomUser

class OrderPageTestCase(TestCase):
    def setUp(self):
        Order.objects.create(
            braintree_id = '1uds738',
            first_name = 'Michael',
            last_name = 'Scott',
            email = 'michaelscott@gmail.com',
            address = 'Paken street',
            postal_code = 'werwr',
            city = 'LA',
            created = timezone.now(),
            updated = timezone.now(),
            paid=False
        )

    def test_model(self):
        person = Order.objects.get(id=1)
        self.assertEqual(person.email, 'michaelscott@gmail.com')

class OrderItemTestCase(TestCase):
    def setUp(self):
        Order.objects.create(
            braintree_id = '1uds738',
            first_name = 'John',
            last_name = 'Doe',
            email = 'johndoe@gmail.com',
            address = 'Paken street',
            postal_code = 'werwr',
            city = 'LA',
            created = timezone.now(),
            updated = timezone.now(),
            paid=False
        )
        self.user = CustomUser.objects.create(email='test@email.com', first_name='test', last_name='user', password='')
        self.user.set_password('secret')
        self.user.save()
        Category.objects.create(name='Electronics', slug='electronics', created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(owner=self.user,category=Category.objects.get(id=1),name='Toaster', slug='slug',description='Amazing toaster',
        price=49.99, available=True, created_at=timezone.now(), updated_at=timezone.now(), image=None)
        
        OrderItem.objects.create(
            order=Order.objects.get(id=1),
            product = Product.objects.get(id=1),
            price = 49.99
        )

    def test_model(self):
        item = OrderItem.objects.get(id=1)
        self.assertEqual(item.product.name, 'Toaster')