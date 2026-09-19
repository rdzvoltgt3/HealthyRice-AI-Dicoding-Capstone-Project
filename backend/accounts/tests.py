from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class RegisterTests(APITestCase):
    def test_register_creates_user_and_returns_tokens(self):
        response = self.client.post("/api/auth/register/", {
            "full_name": "Petani Test",
            "email": "petani@test.com",
            "password": "padihijau123",
            "confirm_password": "padihijau123",
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertTrue(User.objects.filter(email="petani@test.com").exists())

    def test_register_rejects_mismatched_passwords(self):
        response = self.client.post("/api/auth/register/", {
            "full_name": "Petani Test",
            "email": "petani@test.com",
            "password": "padihijau123",
            "confirm_password": "beda123456",
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("confirm_password", response.data)

    def test_register_rejects_duplicate_email(self):
        User.objects.create_user(username="existing", email="petani@test.com", password="x")
        response = self.client.post("/api/auth/register/", {
            "full_name": "Petani Lain",
            "email": "petani@test.com",
            "password": "padihijau123",
            "confirm_password": "padihijau123",
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="petani", email="petani@test.com", password="padihijau123"
        )

    def test_login_with_correct_credentials(self):
        response = self.client.post("/api/auth/login/", {
            "email": "petani@test.com",
            "password": "padihijau123",
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_login_with_wrong_password_fails(self):
        response = self.client.post("/api/auth/login/", {
            "email": "petani@test.com",
            "password": "salahpassword",
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_me_requires_authentication(self):
        response = self.client.get("/api/auth/me/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_me_returns_current_user_when_authenticated(self):
        login = self.client.post("/api/auth/login/", {
            "email": "petani@test.com", "password": "padihijau123",
        })
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {login.data['access']}")
        response = self.client.get("/api/auth/me/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "petani@test.com")
