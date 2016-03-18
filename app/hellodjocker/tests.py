from django.core.urlresolvers import reverse
from django.test import TestCase


class HelloDjockerTestCase(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign your name")

    def test_visit_count(self):
        response = self.client.get(reverse("home"))
        visit_count = response.context['visits']
        response = self.client.get(reverse("home"))
        self.assertGreater(response.context['visits'], visit_count)

    def test_name_signature(self):
        response = self.client.post(reverse("home"), {'name': "Bob Smith"}, follow=True)
        self.assertRedirects(response, reverse("home"))
        self.assertContains(response, "Bob Smith")
