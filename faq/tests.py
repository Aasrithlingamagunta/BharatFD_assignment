from django.test import TestCase
from faq.models import FAQ
from rest_framework.test import APITestCase
from rest_framework import status


class FAQModelTest(TestCase):
    def setUp(self):
        """
        Create a sample FAQ entry for testing.
        """
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python web framework.",
        )

    def test_auto_translation(self):
        """
        Verify that translations are generated on save.
        """
        self.assertIsNotNone(self.faq.question_hi)
        self.assertIsNotNone(self.faq.question_bn)

    def test_string_representation(self):
        """
        Check that FAQ model returns the correct string representation.
        """
        self.assertEqual(str(self.faq), "What is Django?")


class FAQAPITest(APITestCase):
    def setUp(self):
        """
        Create a sample FAQ entry for API testing.
        """
        self.faq = FAQ.objects.create(
            question="What is REST API?",
            answer="REST API is a standard for web services.",
        )

    def test_get_faqs_english(self):
        """
        Test fetching FAQs in English (default).
        """
        response = self.client.get("/api/faqs/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_get_faqs_hindi(self):
        """
        Test fetching FAQs in Hindi.
        """
        response = self.client.get("/api/faqs/?lang=hi")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
        self.assertIn("क्या है REST API?", response.data[0]["question"])
