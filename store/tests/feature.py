from rest_framework.test import APITestCase
from ..models.department import Department
from ..models.feature import Feature
from django.contrib.auth.models import User
from . import rest_full_test


class FeatureTests(APITestCase):

    def setUp(self):
        self.new_department_name = 'test department'
        self.new_department_description = 'deparment description'
        self.new_feature_name = 'test feature'
        self.new_feature_description = 'feature description'

        self.feature_list_url = '/store/feature/'
        self.feature_detail_url = '/store/feature/{0}/'
        self.feature_add_url = '/store/feature/add/'

    def login_with_super_user(self):
        user_name = 'admin'
        email = 'admin@devzillas.com'
        password = 'adminpassword'
        self.superuser = User.objects.create_superuser(user_name,
                                                       email,
                                                       password)
        self.client.login(username=user_name,
                          password=password)

    def add_department_to_database(self):
        self.department = Department.objects.create(title=self.new_department_name,
                                                    user=self.superuser)

    def add_feature_to_database(self):
        self.add_department_to_database()
        self.feature = Feature.objects.create(title=self.new_feature_name,
                                              user=self.superuser,
                                              department=self.department)

    def test_login_failed(self):
        rest_full_test.test_login_failed(self,
                                         self.feature_list_url)

    def test_feature_list(self):
        self.login_with_super_user()
        self.add_feature_to_database()
        rest_full_test.test_get_list_api(self,
                                         self.feature_list_url,
                                         title=self.feature.title)

    def test_feature_detail_get(self):
        self.login_with_super_user()
        self.add_feature_to_database()
        url = self.feature_detail_url.format(str(self.feature.id))
        rest_full_test.test_get_item_api(self,
                                         url,
                                         title=self.feature.title,
                                         department_id=self.feature.department_id)

    def test_feature_put(self):
        self.login_with_super_user()
        self.add_feature_to_database()
        url = self.feature_detail_url.format(str(self.feature.id))
        rest_full_test.test_put_api(self,
                                    url,
                                    title='test2',
                                    description='my new description',
                                    department_id=self.feature.department_id)

    def test_feature_delete(self):
        self.login_with_super_user()
        self.add_feature_to_database()
        url = self.feature_detail_url.format(str(self.feature.id))
        rest_full_test.test_delete_api(self,
                                       url)

    def test_add_feature(self):
        # prepare data
        self.login_with_super_user()
        self.add_feature_to_database()
        rest_full_test.test_post_api(self,
                                     self.feature_add_url,
                                     title='add new department',
                                     description='description of new department',
                                     department_id=self.feature.department_id)
