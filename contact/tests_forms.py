from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_message_required(self):
        form = ContactForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    def test_name_required(self):
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    def test_email_required(self):
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    def test_subject_required(self):
        form = ContactForm({'subject': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    def test_field_is_explicit_in_form_metaclass(self):
        form = ContactForm()
        self.assertEqual(form.Meta.fields, ['name', 'email',
                                            'subject', 'message'],)
