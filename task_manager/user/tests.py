from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from task_manager.user.models import User


class TestUserModel(TestCase):
    fixtures = ['users.json']


    def test_create_user(self):
        user_data = {
            'first_name': 'Dmitriy',
            'last_name': 'Horoshev',
            'username': 'user_1',
            'password1': '12345678Aa',
            'password2': '12345678Aa',
        }
        response = self.client.post(reverse('add_user'), user_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(User.objects.filter(username=user_data['username']).exists())


    def test_update_user(self):
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        update_data = {
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'username': 'Ivan2000',
            'password1': '12345678Aa',
            'password2': '12345678Aa'
        }
        response = self.client.post(reverse('edit_user', args=[user.pk]), update_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        user.refresh_from_db()
        self.assertEqual(user.username, 'Ivan2000')


    def test_delete_user(self):
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        response = self.client.post(reverse('delete_user', args=[user.pk]))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertFalse(User.objects.filter(username='IvanIvanov').exists())