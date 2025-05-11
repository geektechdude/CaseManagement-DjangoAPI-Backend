from django.test import TestCase
from cmapp.models import Task


class TaskTestCase(TestCase):

    def setUp(self):
        Task.objects.create(cmTitle = "A test title",
                            cmDescription = "A test description has been entered",
                            cmStatus = "Open", 
                            cmDueDate = "2025-05-30T13:05:00Z")

    def test_return_task_title(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.cmTitle, "A test title")

    def test_return_task_description(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.cmDescription, "A test description has been entered")

    def test_return_task_status(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.cmStatus, "Open")

    def test_return_task_dueDate(self):
        task = Task.objects.get(id=1)
        self.assertEqual(str(task.cmDueDate), "2025-05-30 13:05:00+00:00")
