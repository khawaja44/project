from django.db import models
from django.contrib.auth.models import User

useer_type = (('developer', 'Developer'),('manager' , 'Manager'),('qa' , 'Quality Assurance'))

class Useer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    useertype = models.CharField(max_length=30, choices=useer_type, default='developer', verbose_name = 'User Type')

    def __str__(self):
        return self.name


bug_type = (('feature', 'Feature'), ('bug', 'Bug'))

class Bug(models.Model):
    title = models.CharField(max_length=20)
    deadline = models.DateField()
    type = models.CharField(max_length=20, choices=bug_type, default='bug')

    bugcreater = models.ForeignKey('Useer', on_delete=models.CASCADE,related_name='Creater', verbose_name = 'Bug Creater')
    bugsolver = models.ForeignKey('Useer', on_delete=models.CASCADE,related_name='Solver', verbose_name = 'Bug Solver')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='project')

    def __str__(self):
        return self.title

class Project(models.Model):
    pname = models.CharField(max_length=50, verbose_name='Project Name')
    useer = models.ManyToManyField('Useer')

    def __str__(self):
        return self.pname