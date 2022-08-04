from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import *


class TestUrls(SimpleTestCase):

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func,loginPage)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logoutUser)

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, registerPage)

    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_room_url(self):
        url = reverse('room', args=['1'])
        self.assertEqual(resolve(url).func, room)

    def test_user_profile_url(self):
        url = reverse('user-profile', args=['1'])
        self.assertEqual(resolve(url).func, userProfile)

    def test_create_room_url(self):
        url = reverse('create-room')
        self.assertEqual(resolve(url).func, createRoom)

    def test_update_room_url(self):
        url = reverse('update-room', args=['1'])
        self.assertEqual(resolve(url).func, updateRoom)

    def test_delete_room_url(self):
        url = reverse('delete-room', args=['1'])
        self.assertEqual(resolve(url).func, deleteRoom)

    def test_delete_message_url(self):
        url = reverse('delete-message', args=['1'])
        self.assertEqual(resolve(url).func, deleteMessage)

    def test_update_user_url(self):
        url = reverse('update-user')
        self.assertEqual(resolve(url).func, updateUser)

    def test_topics_url(self):
        url = reverse('topics')
        self.assert_(resolve(url).func, topicsPage)

    def test_activity_url(self):
        url = reverse('activity')
        self.assertEqual(resolve(url).func, activitiyPage)