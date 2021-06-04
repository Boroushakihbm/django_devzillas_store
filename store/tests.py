from rest_framework.test import APITestCase
from rest_framework import status
from .models import Department, Feature
from django.contrib.auth.models import User
import json


class DepartmentListTests(APITestCase):

    def test_login_failed(self):
        response = self.client.get('/store/department/', format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_department_list(self):

        # prepare data
        self.superuser = User.objects.create_superuser('admin', 'admin@devzillas.com', 'adminpassword')
        self.client.login(username='admin', password='adminpassword')
        self.department = Department.objects.create(title='test', user=self.superuser)

        # run methods
        response = self.client.get('/store/department/', format='json')
        data = json.loads(response.content)

        # assertion
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[0]['title'], self.department.title)
