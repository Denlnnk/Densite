from django.test import TestCase, Client
from django.urls import reverse
from base.models import *


class TestViews(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            id=1,
            name='Vova'
        )
        self.topic = Topic.objects.create(
            name='Something'
        )
        self.room = Room.objects.create(
            id=1,
            host=self.user,
            topic=self.topic
        )
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.home_url = reverse('home')
        self.user_url = reverse('user-profile', args=['1'])
        self.room_url = reverse('room', args=['1'])
        self.create_room_url = reverse('create-room')

    def test_project_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html')


    def test_project_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/login-register.html')



    def test_project_logout(self):
        response = self.client.get(self.logout_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.home_url)


    def test_project_user_GET(self):
        response = self.client.get(self.user_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/profile.html')


    def test_project_room_GET(self):
        response = self.client.get(self.room_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/room.html')


    def test_project_room_POST(self):
        response = self.client.post(self.create_room_url, {
            'host': 'Vova',
            'topic': 'Something',
        })

        self.assertEqual(response.status_code, 302)

