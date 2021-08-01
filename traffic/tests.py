from django.test import TestCase
from traffic.forms import LightsForm

# Create your tests here.
class TestPage(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
class TestForm(TestCase):
    def test_validate_light_form(self):
        form = LightsForm(data={"state": "A"})
        self.assertTrue(form.is_valid())

    def test_invalid_light_form(self):
        form = LightsForm(data={"state": "off"})
        self.assertFalse(form.is_valid())
