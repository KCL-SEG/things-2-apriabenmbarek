from django.test import TestCase
from things.forms import ThingForm
from things.models import Thing

class ThingFormTestCase(TestCase):

    def setUp(self):
        self.form_input = {
            'name': 'Apple',
            'description': 'A round fruit.',
            'quantity': '5'
        }

    def test_valid_thing_form(self):
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_has_necessary_fields(self):
        form = ThingForm()
        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('quantity', form.fields)
