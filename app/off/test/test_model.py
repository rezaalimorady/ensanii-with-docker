from django.test import TestCase
from off.models import Off, UseCodeByUser
from django.contrib.auth.models import User
from django.utils import timezone


class OffTest(TestCase):
    """test for OFF app models"""

    def setUp(self):
        self.user = User.objects.create_user('testUser', 'test@mail.co', 'testUserPass')
        self.off = Off.objects.create(
            name='testOff',
            code='testCode',
            date_create=timezone.now(),
            expired_at=timezone.now(),
            ctrated_by=self.user
        )
        self.used_code = UseCodeByUser.objects.create(
            code=self.off,
            user=self.user,
            date=timezone.now()
        )

    def test_is_user_created(self):
        """test is test user created or not"""
        get_user = User.objects.get(username='testUser')
        self.assertEqual(get_user, self.user)

    def test_off_mode_creation(self):
        """test is OFF model created"""
        self.assertEqual(self.off.name, 'testOff')
        self.assertEqual(self.off.code, 'testCode')
        self.assertEqual(self.off.ctrated_by, self.user)
        self.assertTrue(self.off.date_create)
        self.assertTrue(self.off.expired_at)

    def test_used_code_creation(self):
        """test is used code create or not"""
        self.assertEqual(self.used_code.code, self.off)
        self.assertEqual(self.used_code.user, self.user)
        self.assertTrue(self.used_code.date)
