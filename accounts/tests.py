from django.contrib.auth import get_user_model
from django.test import TestCase


# Create your tests here.
class CustomerUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="test1", email="test1@test.com", password="testpass123"
        )
        self.assertEqual(user.username, "test1")
        self.assertEqual(user.email, "test1@test.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="superadmin", email="superadmin@test.com", password="testpass123"
        )
        self.assertEqual(user.username, "superadmin")
        self.assertEqual(user.email, "superadmin@test.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
    