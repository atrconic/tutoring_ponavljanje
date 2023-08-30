# from django.test import TestCase
# import pytest
# from rest_framework.test import APIClient
# from .models import F1Driver
#
# client = APIClient()
#
# @pytest.mark.django_db
# def test_create_f1driver():
#     response = client.post('/resttest/create-f1driver/')
#     assert response.status_code == 201
#     f1driver = F1Driver.objects.first()
#      assert f1driver is not None
