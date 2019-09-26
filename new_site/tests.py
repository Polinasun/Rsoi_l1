from django.test import TestCase
from new_site.models import Car
# Create your tests here.
class ProductTest(TestCase):

    def test_new_car(self):
        file_={'model': 'Toyota'}
        pares=self.client.post(
        path ='/new_site/new_car/',
        date = file_
        )
        self.assertEqual(pares.status_code, 200)
        #self.assertNoIn(b'Model not found', pares.content)
        #self.assertNoIn(b'Please write POST', pares.content)
    def test_get_car(self):
        pares=self.client.get('/new_site/get_car/?model=Toyota')
        self.assertEqual(pares.status_code, 200)
