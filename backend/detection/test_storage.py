from unittest.mock import MagicMock, patch

from django.core.files.base import ContentFile
from django.test import TestCase

from .storage import VercelBlobStorage


class VercelBlobStorageTests(TestCase):


    def test_save_uploads_to_blob_and_returns_its_public_url(self):
        storage = VercelBlobStorage()
        fake_client = MagicMock()
        fake_client.put.return_value = MagicMock(
            url="https://abc123.public.blob.vercel-storage.com/detections/user_1/leaf.jpg"
        )
        storage._client = fake_client

        content = ContentFile(b"fake image bytes", name="leaf.jpg")
        content.content_type = "image/jpeg"

        saved_name = storage._save("detections/user_1/leaf.jpg", content)

        fake_client.put.assert_called_once()
        call_args = fake_client.put.call_args
        self.assertEqual(call_args[0][0], "detections/user_1/leaf.jpg")
        self.assertEqual(call_args[1]["access"], "public")
        self.assertEqual(call_args[1]["content_type"], "image/jpeg")


        self.assertEqual(saved_name, "https://abc123.public.blob.vercel-storage.com/detections/user_1/leaf.jpg")

    def test_url_returns_the_stored_name_directly(self):
        storage = VercelBlobStorage()
        url = "https://abc123.public.blob.vercel-storage.com/detections/user_1/leaf.jpg"
        self.assertEqual(storage.url(url), url)

    def test_delete_calls_blob_delete_with_the_name(self):
        storage = VercelBlobStorage()
        fake_client = MagicMock()
        storage._client = fake_client

        storage.delete("https://abc123.public.blob.vercel-storage.com/detections/user_1/leaf.jpg")

        fake_client.delete.assert_called_once_with(
            ["https://abc123.public.blob.vercel-storage.com/detections/user_1/leaf.jpg"]
        )
