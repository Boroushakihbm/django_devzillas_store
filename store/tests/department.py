from rest_framework.test import APITestCase
from . import rest_full_test
from ..models.department import Department
from django.contrib.auth.models import User


class DepartmentTests(APITestCase):
    def setUp(self):
        self.new_department_name = 'test department'
        self.new_department_description = 'department description'
        self.department_list_url = '/store/department/'
        self.department_detail_url = '/store/department/{0}/'
        self.department_add_url = '/store/department/add/'

    def login_with_super_user(self):
        user_name = 'admin'
        email = 'admin@devzillas.com'
        password = 'adminpassword'
        self.superuser = User.objects.create_superuser(user_name,
                                                       email,
                                                       password)
        self.client.login(username=user_name, password=password)

    def add_department_to_database(self):
        self.department = Department.objects.create(title=self.new_department_name, user=self.superuser)

    def test_login_failed(self):
        rest_full_test.test_login_failed(self,
                                         self.department_list_url)

    def test_department_list(self):
        # prepare data
        self.login_with_super_user()
        self.add_department_to_database()
        rest_full_test.test_get_list_api(self,
                                         self.department_list_url,
                                         title=self.department.title)

    def test_department_detail_get(self):
        self.login_with_super_user()
        self.add_department_to_database()
        url = self.department_detail_url.format(str(self.department.id))
        rest_full_test.test_get_item_api(self,
                                         url,
                                         title=self.department.title)

    def test_department_put(self):
        # prepare data
        self.login_with_super_user()
        self.add_department_to_database()
        url = self.department_detail_url.format(str(self.department.id))
        rest_full_test.test_put_api(self,
                                    url,
                                    title='test2',
                                    description='my new description',
                                    parent_department_id=None)

    def test_department_delete(self):
        # prepare data
        self.login_with_super_user()
        self.add_department_to_database()
        url = self.department_detail_url.format(str(self.department.id))
        rest_full_test.test_delete_api(self,
                                       url)

    def test_add_department(self):
        # prepare data
        self.login_with_super_user()
        self.add_department_to_database()
        rest_full_test.test_post_api(self,
                                     self.department_add_url,
                                     title=self.new_department_name,
                                     description=self.new_department_description,
                                     parent_department_id=None)

