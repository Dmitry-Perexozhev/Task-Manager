from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.user.models import User


class TestStatusModel(TestCase):
    fixtures = ['statuses.json', 'task_manager/user/fixtures/users.json']


    def test_create_status(self):
        status_data = {
            'name': 'тестируется'
        }
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        response = self.client.post(reverse('add_status'), status_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(Status.objects.filter(name=status_data['name']).exists())


    def test_update_status(self):
        status = Status.objects.get(name='принят')
        update_data = {
            'name': 'завершен'
        }
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        response = self.client.post(reverse('update_status', args=[status.pk]), update_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        status.refresh_from_db()
        self.assertEqual(status.name, update_data['name'])


    def test_delete_status(self):
        status = Status.objects.get(name='принят')
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        response = self.client.post(reverse('delete_status', args=[status.pk]))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertFalse(Status.objects.filter(name='принят').exists())


    def test_read_status(self):
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        response = self.client.get(reverse('statuses_list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'status/status_list.html')