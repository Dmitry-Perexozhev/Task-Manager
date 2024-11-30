from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.user.models import User


class TestTaskModel(TestCase):
    fixtures = [
        'task.json',
        'task_manager/statuses/fixtures/statuses.json',
        'task_manager/user/fixtures/users.json'
    ]

    def test_create_task(self):
        task_data = {
            'name': 'Первая задача',
            'description': 'Описание первой задачи',
            'status': Status.objects.get(name='принят').pk,
            'executor': User.objects.get(username='PetrPetrov').pk
        }
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        response = self.client.post(reverse('add_task'), task_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(Task.objects.filter(name=task_data['name']).exists())

    def test_update_task(self):
        task = Task.objects.get(name='Тестовая задача')
        update_data = {
            'name': 'Измененная задача',
            'description': 'Описание первой задачи',
            'status': Status.objects.get(name='принят').pk,
            'executor': User.objects.get(username='PetrPetrov').pk
        }
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        response = self.client.post(
            reverse('update_task', args=[task.pk]), update_data
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        task.refresh_from_db()
        self.assertEqual(task.name, update_data['name'])

    def test_delete_task(self):
        task = Task.objects.get(name='Тестовая задача')
        user = User.objects.get(username='PetrPetrov')
        self.client.login(username=user.username, password='1234')
        response = self.client.post(reverse('delete_task', args=[task.pk]))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertFalse(Task.objects.filter(name='Тестовая задача').exists())

    def test_read_task(self):
        task = Task.objects.get(name='Тестовая задача')
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        response = self.client.get(reverse('task_view', args=[task.pk]))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'task/task_view.html')

    def test_read_tasks_list(self):
        user = User.objects.get(username='IvanIvanov')
        self.client.login(username=user.username, password='1234')
        response = self.client.get(reverse('tasks_list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'task/task_list.html')
