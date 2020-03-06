from django.db import models

class Courses(models.Model):
    course_id = models.CharField(max_length = 200)
    course_name = models.CharField(max_length = 200)

    def __str__(self):
        return "course_id:{}, course_name: {}".format(self.course_id, self.course_name)

class Labs(models.Model):
    course = models.ForeignKey(Courses, on_delete = models.CASCADE)
    lab_id = models.CharField(max_length = 200)
    lab_name = models.CharField(max_length = 200)


    def __str__(self):
        return self.lab_id 