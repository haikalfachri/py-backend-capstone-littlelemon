from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class MenuAPITest(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='littlelemon',
            email='admin@example.com'
        )
        self.client = APIClient()

    def test_get_menu_list(self):
        url = reverse('menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_menu_item_as_admin(self):
        self.client.login(username='admin', password='littlelemon')
        url = reverse('menu')
        data = {
            'title': 'Pasta',
            'price': 15.99,
            'description': 'Delicious homemade pasta'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)