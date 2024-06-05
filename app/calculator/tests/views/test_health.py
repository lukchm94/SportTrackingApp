from django.test import Client, TestCase
from django.urls import reverse


class CalculateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.health_url = reverse("health")

    def test_health_status(self):
        resp = self.client.get(self.health_url)

        self.assertEqual(resp.status_code, 200)
        self.assertJSONEqual(resp.content, {"status": "healthy"})
