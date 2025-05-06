from django.db import models



class Task(models.Model):
    OPEN = 'Open'
    CLOSED = 'Closed'
    INPROGRESS = 'InProgress'
    BLOCKED = 'Blocked'
    
    STATUS_OPTIONS = [
    (OPEN, 'Open'),
    (CLOSED, 'Closed'),
    (INPROGRESS, 'In Progress'),
    (BLOCKED, 'BLOCKED')
    ]

    cmTitle = models.CharField(max_length=255, default='')
    cmDescription = models.TextField(blank=True)
    cmStatus = models.CharField(choices=STATUS_OPTIONS, default='OPEN')
    cmDueDate = models.DateTimeField()

    def __str__(self):
        title = str(self.cmTitle)
        return title

    class Meta:
        ordering = ['cmTitle']