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

    def test_createTask(self):
        response = self.client.post('/api/v1/tasks/', {"cmTitle":"test2", "cmDescription":"test2", "cmStatus":"Open", "cmDueDate":"2025-05-28T13:05:00Z"})
        self.assertEqual(response.status_code, 201)
    
    def test_taskStatus(self):
        self.client.post('/api/v1/tasks/', {"cmTitle":"test2", "cmDescription":"test2", "cmStatus":"Open", "cmDueDate":"2025-05-28T13:05:00Z"})
        response = self.client.get('/api/v1/task/2')
        self.assertEqual(response.status_code, 200)

    def test_taskPut(self):
        self.client.post('/api/v1/tasks/', {"cmTitle":"test2", "cmDescription":"test2", "cmStatus":"Open", "cmDueDate":"2025-05-28T13:05:00Z"})
        self.client.put('/api/v1/task/2', {"cmDescription":"test2, updated"})
        response = self.client.get('/api/v1/task/2')
        self.assertTrue(response.content, "test2, updated")

    def test_taskDelete(self):
        self.client.post('/api/v1/tasks/', {"cmTitle":"test2", "cmDescription":"test2", "cmStatus":"Open", "cmDueDate":"2025-05-28T13:05:00Z"})
        self.client.delete('/api/v1/task/2')
        response = self.client.get('/api/v1/task/2')
        self.assertEqual(response.status_code, 404)