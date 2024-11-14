from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from task_manager.labels.models import Label
from task_manager.user.models import User


class TestLabelModel(TestCase):
    fixtures = ['label.json', 'task_manager/user/fixtures/users.json']


    def test_create_label(self):
        status_data = {
            'name': 'в архив'
        }
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        response = self.client.post(reverse('add_label'), status_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(Label.objects.filter(name=status_data['name']).exists())


    def test_update_label(self):
        label = Label.objects.get(name='срочно')
        update_data = {
            'name': 'первая задача'
        }
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        response = self.client.post(reverse('update_label', args=[label.pk]), update_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        label.refresh_from_db()
        self.assertEqual(label.name, update_data['name'])


    def test_delete_label(self):
        label = Label.objects.get(name='срочно')
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        response = self.client.post(reverse('delete_label', args=[label.pk]))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertFalse(Label.objects.filter(name='срочно').exists())


    def test_read_label(self):
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        response = self.client.get(reverse('labels_list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'label/label_list.html')