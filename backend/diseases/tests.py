from rest_framework import status
from rest_framework.test import APITestCase

from .models import Disease


class DiseaseCatalogTests(APITestCase):
    def setUp(self):
        Disease.objects.create(
            slug="tungro", name="Tungro", short_description="Daun menguning.",
            symptoms="Gejala 1\nGejala 2", treatment_steps="Langkah 1\nLangkah 2",
            risk_level=Disease.RiskLevel.MEDIUM,
        )

    def test_list_diseases_is_public(self):
       
        response = self.client.get("/api/diseases/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_by_slug_returns_bullet_lists(self):
        response = self.client.get("/api/diseases/tungro/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Tungro")

        self.assertEqual(response.data["symptoms"], ["Gejala 1", "Gejala 2"])
        self.assertEqual(response.data["treatment_steps"], ["Langkah 1", "Langkah 2"])

    def test_unknown_slug_returns_404(self):
        response = self.client.get("/api/diseases/not-a-real-disease/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
