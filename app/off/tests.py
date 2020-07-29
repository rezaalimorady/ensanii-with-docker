from django.test import TestCase
from .models import Off, UseCodeByUser
from django.utils import timezone
from django.contrib.auth.models import User


# Create your tests here.
class OffTest(TestCase):
    def setUp(self):
        """create test model"""
        user = User.objects.create_user('test', 'email@test.com', 'testpassword')
        Off.objects.create(
            name="test",
            code="testcode",
            date_create=timezone.now(),
            expired_at=timezone.now(),
            status=True,
            ctrated_by=user
        )
        test_off = Off.objects.get(name='test')
        UseCodeByUser.objects.create(
            code=test_off,
            user=user,
            date=timezone.now()
        )


    def test_off_created(self):
        """test check off object created"""
        test_off = Off.objects.get(name='test')
        self.assertEqual(test_off.name, 'test')
        self.assertEqual(test_off.code, 'testcode')

    def test_use_code_by_user(self):
        """test create model used by user"""
        test_off = Off.objects.get(name='test')
        create_by_user = UseCodeByUser.objects.get(code=test_off)
        self.assertEqual(create_by_user.code, test_off)
