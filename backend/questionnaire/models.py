from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SECTION_CHOICES = (
    ('section1' , 'section1'),
    ('section2' , 'section2')
)

class Question(models.Model):
    section = models.CharField(choices=SECTION_CHOICES , max_length=10)
    question = models.CharField(max_length=100)
    ans1 = models.CharField(max_length=50, blank=True , null=True)
    ans2 = models.CharField(max_length=50, blank=True , null=True)
    ans3 = models.CharField(max_length=50 , blank=True , null=True)
    text_question = models.BooleanField(default=False)


    def __str__(self):
        return self.question 



class BusinessPlanModel(models.Model):
    user =  models.ForeignKey(User , on_delete=models.CASCADE)
    planid = models.IntegerField(default=1)
    def __str__(self):
        return f"{str(self.user)}-{self.planid}"


class BusinessPlanQuestions(models.Model):
    businessplanid =  models.ForeignKey(BusinessPlanModel , on_delete=models.CASCADE)
    question =  models.ForeignKey(Question , on_delete=models.CASCADE)
    answer = models.CharField(max_length=50)


    def __str__(self):
        return str(self.businessplanid)

