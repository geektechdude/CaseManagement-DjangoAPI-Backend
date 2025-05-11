from django.test import TestCase
from cmapp.models import Task



class viewTest(TestCase):

    def setUp(self):
        Task.objects.create(cmTitle = "A test title",
                    cmDescription = "A test description has been entered",
                    cmStatus = "Open", 
                    cmDueDate = "2025-05-30T13:05:00Z")

    def test_tasklist(self):
        response = self.client.get('/api/v1/tasks/')
        self.assertTrue(response.content, "A test title")
    
    def test_tasklistStatus(self):
        response = self.client.get('/api/v1/tasks/')
        self.assertEqual(response.status_code, 200)
    
    def test_task(self):
        response = self.client.get('/api/v1/task/1')
        self.assertTrue(response.content, "A test description has been entered")

    def test_taskStatus(self):
        response = self.client.get('/api/v1/task/1')
        self.assertEqual(response.status_code, 200)