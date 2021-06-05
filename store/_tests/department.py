from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Department
from django.contrib.auth.models import User
import json


class DepartmentTests(APITestCase):
    def setUp(self):
        self.new_department_name = 'test department'
        self.new_department_description = 'deparment description'
        self.user_name = 'admin'
        self.email = 'admin@devzillas.com'
        self.email = 'adminpassword'
        self.department_list_url = '/store/department/'
        self.department_detail_url = '/store/department/{0}/'
        self.department_add_url = '/store/department/add/'

    def login_with_super_user(self):
        self.superuser = User.objects.create_superuser(self.user_name,
                                                       self.email,
                                                       self.email)
        self.client.login(username=self.user_name, password=self.email)

    def add_department_to_database(self):
        self.department = Department.objects.create(title=self.new_department_name, user=self.superuser)

    def test_login_failed(self):
        response = self.client.get(self.department_list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_department_list(self):
        # prepare data
        self.login_with_super_user()
        self.add_department_to_database()

        # run methods
        response = self.client.get(self.department_list_url, format='json')

        # assertion
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], self.department.title)

    def test_department_detail_get(self):
        # prepare data
        self.login_with_super_user()
        self.add_department_to_database()

        # run methods
        response_get = self.client.get(self.department_detail_url.format(str(self.department.id)),
                                       format='json')
        # get method assertion
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)

        data = json.loads(response_get.content)
        self.assertEqual(data['title'], self.department.title)

    def test_department_put(self):
        # prepare data
        self.login_with_super_user()
        self.add_department_to_database()

        new_title = 'test2'
        new_description = 'my new description'
        data_put = {'title': new_title,
                    'description': new_description,
                    'parent_department_id': None}
        response_put = self.client.put(self.department_detail_url.format(str(self.department.id)),
                                       data_put,
                                       format='json')
        # put method assertion
        self.assertEqual(response_put.status_code, status.HTTP_200_OK)

        data = json.loads(response_put.content)
        self.assertEqual(data['title'], new_title)
        self.assertEqual(data['description'], new_description)

    def test_department_delete(self):
        # prepare data
        self.login_with_super_user()
        self.add_department_to_database()

        response_put = self.client.delete(self.department_detail_url.format(str(self.department.id)),
                                          format='json')
        # put method assertion
        self.assertEqual(response_put.status_code, status.HTTP_204_NO_CONTENT)

    def test_add_department(self):
        # prepare data
        self.login_with_super_user()
        self.add_department_to_database()
        data = {'title': self.new_department_name,
                'description': self.new_department_description,
                'parent_department_id': None,
                }

        # run methods
        response = self.client.post(self.department_add_url,
                                    data,
                                    format='json')

        # assertion
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = json.loads(response.content)
        self.assertEqual(data['title'], self.new_department_name)
        self.assertEqual(data['description'], self.new_department_description)
