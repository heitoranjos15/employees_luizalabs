import random
import json
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from faker import Faker
from employee.models import Employee
from employee.api.serializers import EmployeeSerializer

class BaseViewTest(APITestCase):
    client = APIClient()
    
    @staticmethod
    def create_employee():
        fake = Faker()
        random_employee = range(3,10)
        for _ in range(random.choice(random_employee)):
            Employee.objects.create(name= fake.name(), email= fake.email(), department= fake.job())


class GetAllEmployeeTest(BaseViewTest):

    def test_get_employee(self):
        self.create_employee()
        response = self.client.get(
            reverse("employee_list")
        )
        expected = Employee.objects.all()
        serialized = EmployeeSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class InsertEmployeeTest(BaseViewTest):

    def setUp(self):
        fake = Faker()
        self.valid_payload = {
            'name': fake.name(),
            'email': fake.email(),
            'department': fake.job()
        }

    def test_insert_employee(self):
        response = self.client.post(
            reverse("employee_list"),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_insert_invalid_employee(self):
        response = self.client.post(
            reverse("employee_list"),
            data=json.dumps({
                'name': 'invalid'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            "email": ["This field is required."],
            "department": ["This field is required."]
        })

    def test_insert_invalid_field_employee(self):
        response = self.client.post(
            reverse("employee_list"),
            data=json.dumps({
                'name': 'invalid',
                'email': 1234,
                'department': 'invalid'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, { 
            "email": ["Enter a valid email address."]
        })

class AlterEmployeeTest(BaseViewTest):
    
    def setUp(self):
        self.fake = Faker()
        self.create_employee()
    
    def test_alter_employee(self):
        response = self.client.put(
            reverse('employee_edit', kwargs={'pk': 1}),
            data=json.dumps({
                'name': self.fake.name(),
                'email': self.fake.email(),
                'department': self.fake.job()
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_alter_invalid_employee(self):
        response = self.client.put(
            reverse('employee_edit', kwargs={'pk': 1}),
            data=json.dumps({
                'name': 'invalid',
                'email': 123,
                'department': 'invalid'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, { 
            "email": ["Enter a valid email address."]
        })
    
    def test_alter_dont_existing_employee(self):
        response = self.client.put(
            reverse('employee_edit', kwargs={'pk': 100})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_employee(self):
        response = self.client.delete(
            reverse('employee_edit', kwargs={'pk': 1}),
            )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_dont_existing_employee(self):
        response = self.client.delete(
            reverse('employee_edit', kwargs={'pk': 100})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)