from django.db import models
import time

class Project(models.Model):
    name = models.CharField(max_length=120)
    start_date = models.DateField(auto_now_add=True, blank=True)
    end_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Task(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=True, blank=True)
    end_date = models.DateField(blank=True, null=True)
    hours_worked = models.IntegerField(default='0',blank=True)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['start_date']

