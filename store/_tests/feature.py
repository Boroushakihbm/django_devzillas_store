from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Feature, Department
from django.contrib.auth.models import User
import json


class FeatureTests(APITestCase):

    def test_login_failed(self):
        response = self.client.get('/store/feature/', format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_department_list(self):
        # prepare data
        self.superuser = User.objects.create_superuser('admin',
                                                       'admin@devzillas.com',
                                                       'adminpassword')
        self.client.login(username='admin', password='adminpassword')
        self.department = Department.objects.create(title='test', user=self.superuser)
        self.feature = Feature.objects.create(title='test', user=self.superuser, department=self.department)

        # run methods
        response = self.client.get('/store/feature/', format='json')

        # assertion
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(data[0]['title'], self.department.title)

    def test_department_detail(self):
        # prepare data
        self.superuser = User.objects.create_superuser('admin',
                                                       'admin@devzillas.com',
                                                       'adminpassword')
        self.client.login(username='admin', password='adminpassword')
        self.department = Department.objects.create(title='test', user=self.superuser)
        self.feature = Feature.objects.create(title='test', user=self.superuser, department=self.department)

        # run methods
        response_get = self.client.get('/store/feature/' +
                                       str(self.feature.id) +
                                       '/', format='json')

        NEW_TITLE = 'test2'
        NEW_DESCRIPTION = 'my new description'
        data_put = {'title': NEW_TITLE, 'description': NEW_DESCRIPTION, 'department_id': 1}
        response_put = self.client.put('/store/feature/' +
                                       str(self.department.id) +
                                       '/',
                                       data_put,
                                       format='json')

        # get method assertion
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)

        data = json.loads(response_get.content)
        self.assertEqual(data['title'], self.feature.title)

        # put method assertion
        self.assertEqual(response_put.status_code, status.HTTP_200_OK)

        data = json.loads(response_put.content)
        self.assertEqual(data['title'], NEW_TITLE)
        self.assertEqual(data['description'], NEW_DESCRIPTION)

    def test_add_department(self):
        # prepare data
        self.superuser = User.objects.create_superuser('admin',
                                                       'admin@devzillas.com',
                                                       'adminpassword')
        self.client.login(username='admin', password='adminpassword')
        self.department = Department.objects.create(title='test', user=self.superuser)
        self.feature = Feature.objects.create(title='test', user=self.superuser, department=self.department)

        # run methods
        TITLE = 'add new department'
        DESCRIPTION = 'description of new department'
        data = {'title': TITLE,
                'description': DESCRIPTION,
                'department_id': self.department.id
                }
        response = self.client.post('/store/feature/add/'
                                    , data, format='json')

        # assertion
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = json.loads(response.content)
        self.assertEqual(data['title'], TITLE)
        self.assertEqual(data['description'], DESCRIPTION)
        self.assertEqual(data['department_id'], self.department.id)
