from django.db import models

# Create your models here.
class Level(models.Model):
    level_name = models.CharField(max_length=5)


class Course:
    course_level = models.ForeignKey(Level,on_delete=models.CASCADE, related_name='level')
    course_name = models.CharField(max_length=255, null=True)

