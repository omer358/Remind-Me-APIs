from django.core.files import File
from django.test import TestCase
from rest_framework.authtoken.admin import User

from .models import People


class PeopleTest(TestCase):
    """Test Module for People Model"""

    def setUp(self) -> None:
        user = User.objects.create(username='none', password='1234')
        user.save()

        People.objects.create(first_name='Omer',
                              second_name='Maki',
                              meeting_place='Home',
                              meeting_time='2021-04-19 03:27:43+02',
                              owner=user
                              )
        People.objects.create(first_name='Mohamed',
                              second_name='Maki',
                              meeting_place='Home',
                              meeting_time='2021-04-29 03:27:43+02',
                              owner=user
                              )

    def test_person(self):
        omer_maki = People.objects.get(first_name='Omer')
        mohamed_maki = People.objects.get(first_name='Mohamed')
        self.assertEqual(
            omer_maki.second_name, "Maki")
        self.assertEqual(
            mohamed_maki.second_name, "Maki")
        self.assertEqual(People.objects.count(), 2)
