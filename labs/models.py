from django.db import models
from django.conf import settings

class Courses(models.Model):
    #TODO allow null values for git_webhook, secret, privatekey and maybe location 
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1000)
    location = models.CharField(max_length=4096, blank=True)
    git_webhook = models.CharField(max_length = 300, blank=True)
    secret = models.CharField(max_length = 20, blank=True)
    private_key = models.CharField(max_length = 6000, blank=True)

    def __str__(self):
        return "course_id:{}, course_name: {}".format(self.id, self.name)

class Labs(models.Model):
    #lab_id   integer
    #course_id  integer
    #name    
    #description
    #number_of_tasks
    #location
    course_id = models.ForeignKey(Courses, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length= 4096)
    number_of_tasks = models.IntegerField()
    location = models.CharField(max_length = 1000)

    def __str__(self):
        return "lab_id:{}, lab_name: {}".format(self.id, self.name)

class CourseOwnership(models.Model):
    #course_id
    #user_id   
    #role 
    course_id = models.ForeignKey(Courses, on_delete= models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    role = models.CharField(max_length=10, blank=True)

    class Meta:
        unique_together = (("course_id", "user_id"))


class Grades(models.Model):
    #studentid _ integer
    #lab_id   _ interger
    #points _ float9
    #tasks completed _ integer
    student_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)    
    lab_id = models.ForeignKey(Labs, on_delete= models.CASCADE)
    points = models.FloatField()
    tasks_completed = models.IntegerField()

    class Meta:
        unique_together = (('student_id', 'lab_id'))



class CourseToLab(models.Model):
    #course_id integer 
    #lab_id  integer
    course_id = models.ForeignKey(Courses, on_delete = models.CASCADE)
    lab_id = models.ForeignKey(Labs, on_delete = models.CASCADE)

    class Meta:
        unique_together = (('course_id', 'lab_id'))