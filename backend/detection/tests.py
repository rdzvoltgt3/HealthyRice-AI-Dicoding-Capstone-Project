import io
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from rest_framework import status
from rest_framework.test import APITestCase

from diseases.models import Disease
from .models import Detection

User = get_user_model()


def make_test_image():

    buffer = io.BytesIO()
    Image.new("RGB", (50, 50), (80, 150, 60)).save(buffer, format="JPEG")
    buffer.seek(0)
    return SimpleUploadedFile("leaf.jpg", buffer.read(), content_type="image/jpeg")


CONFIDENT_RESULT = {
    "label": "tungro", "confidence": 92.5, "inference_time_ms": 250,
    "is_uncertain": False, "reason": None, "message": "Deteksi berhasil.",
}
UNCERTAIN_RESULT = {
    "label": "blast", "confidence": 41.0, "inference_time_ms": 250,
    "is_uncertain": True, "reason": "low_confidence", "message": "Model kurang yakin.",
}
REJECTED_RESULT = {
    "label": "not-rice", "confidence": 95.0, "inference_time_ms": 250,
    "is_uncertain": True, "reason": "not_rice", "message": "Foto ini sepertinya bukan daun padi.",
}


class DetectionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="p1", email="p1@test.com", password="x")
        self.other_user = User.objects.create_user(username="p2", email="p2@test.com", password="x")
        Disease.objects.create(slug="tungro", name="Tungro")
        Disease.objects.create(slug="blast", name="Blast")
        self.client.force_authenticate(user=self.user)

    def test_create_requires_authentication(self):
        self.client.force_authenticate(user=None)
        response = self.client.post("/api/detections/", {"image": make_test_image()})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @patch("detection.views.run_inference", return_value=CONFIDENT_RESULT)
    def test_confident_prediction_saves_to_history(self, mock_infer):
        response = self.client.post("/api/detections/", {"image": make_test_image()})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["disease"]["slug"], "tungro")
        self.assertEqual(Detection.objects.filter(user=self.user).count(), 1)

    @patch("detection.views.run_inference", return_value=UNCERTAIN_RESULT)
    def test_uncertain_prediction_is_not_saved(self, mock_infer):
        response = self.client.post("/api/detections/", {"image": make_test_image()})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["is_uncertain"])

        self.assertEqual(Detection.objects.filter(user=self.user).count(), 0)

    @patch("detection.views.run_inference", return_value=REJECTED_RESULT)
    def test_rejected_class_is_not_saved_either(self, mock_infer):

        response = self.client.post("/api/detections/", {"image": make_test_image()})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["is_uncertain"])
        self.assertEqual(response.data["reason"], "not_rice")
        self.assertEqual(Detection.objects.filter(user=self.user).count(), 0)

    def test_rejects_non_image_file(self):
        bad_file = SimpleUploadedFile("notes.txt", b"hello", content_type="text/plain")
        response = self.client.post("/api/detections/", {"image": bad_file})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch("detection.views.run_inference", return_value=CONFIDENT_RESULT)
    def test_history_filters_by_disease_slug(self, mock_infer):
        self.client.post("/api/detections/", {"image": make_test_image()})  # tungro
        with patch("detection.views.run_inference", return_value={**CONFIDENT_RESULT, "label": "blast"}):
            self.client.post("/api/detections/", {"image": make_test_image()})  # blast

        response = self.client.get("/api/detections/", {"disease": "tungro"})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["disease"]["slug"], "tungro")

    @patch("detection.views.run_inference", return_value=CONFIDENT_RESULT)
    def test_users_only_see_their_own_history(self, mock_infer):
        self.client.post("/api/detections/", {"image": make_test_image()})

        self.client.force_authenticate(user=self.other_user)
        response = self.client.get("/api/detections/")
        self.assertEqual(len(response.data), 0)

    @patch("detection.views.run_inference", return_value=CONFIDENT_RESULT)
    def test_cannot_delete_another_users_detection(self, mock_infer):
        create_response = self.client.post("/api/detections/", {"image": make_test_image()})
        detection_id = create_response.data["id"]

        self.client.force_authenticate(user=self.other_user)
        response = self.client.delete(f"/api/detections/{detection_id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @patch("detection.views.run_inference", return_value=CONFIDENT_RESULT)
    def test_delete_own_detection(self, mock_infer):
        create_response = self.client.post("/api/detections/", {"image": make_test_image()})
        detection_id = create_response.data["id"]

        response = self.client.delete(f"/api/detections/{detection_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Detection.objects.filter(id=detection_id).exists())
