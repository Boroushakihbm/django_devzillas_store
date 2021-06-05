# api test module
import json

from rest_framework import status


def test_login_failed(api_test_case, url):
    response = api_test_case.client.get(url, format='json')
    api_test_case.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


def test_get_list_api(api_test_case, url, **name_value):
    response = api_test_case.client.get(url, format='json')
    api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
    data = json.loads(response.content)
    api_test_case.assertEqual(len(data), 1)
    for (n, v) in name_value.items():
        api_test_case.assertEqual(data[0][n], v)


def test_get_item_api(api_test_case, url, **name_value):
    response = api_test_case.client.get(url, format='json')
    api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
    data = json.loads(response.content)
    for (n, v) in name_value.items():
        api_test_case.assertEqual(data[n], v)


def test_put_api(api_test_case, url, **name_value):
    response = api_test_case.client.put(url, name_value, format='json')
    api_test_case.assertEqual(response.status_code, status.HTTP_200_OK)
    data = json.loads(response.content)
    for (n, v) in name_value.items():
        api_test_case.assertEqual(data[n], v)


def test_delete_api(api_test_case, url):
    response = api_test_case.client.delete(url, format='json')
    api_test_case.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


def test_post_api(api_test_case, url, **name_value):
    response = api_test_case.client.post(url, name_value, format='json')
    api_test_case.assertEqual(response.status_code, status.HTTP_201_CREATED)
    data = json.loads(response.content)
    for (n, v) in name_value.items():
        api_test_case.assertEqual(data[n], v)
