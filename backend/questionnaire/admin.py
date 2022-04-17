from django.contrib import admin

# Register your models here.
from .models import Question , BusinessPlanModel, BusinessPlanQuestions

admin.site.register(Question)
admin.site.register(BusinessPlanModel)
admin.site.register(BusinessPlanQuestions)