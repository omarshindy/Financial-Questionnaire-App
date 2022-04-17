from urllib import response
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer , QuestionSerializer, BusinesPlanSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Question, BusinessPlanModel, BusinessPlanQuestions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json

JWT_authenticator = JWTAuthentication()

#Register API

class RegisterApi(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })




class SectionQuestionListApi(APIView):
    def get(self, request , section_name):
        questions = Question.objects.filter(section=section_name)
        data = QuestionSerializer(questions, many=True ,context={"request": request}).data
        return Response({'data' : data})


class BusinessPlanAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None): 
        user_name = request.user
        # a7a = json.loads(request.body)
        # print(a7a)

        BPM = BusinessPlanModel.objects.create(
            user = user_name,
            planid = 1 if BusinessPlanModel.objects.count() == 0 else BusinessPlanModel.objects.filter(user = user_name).count() + 1
        )

        BPM.save()
        content = {'message': 'Business Plan Created Successfully'}
        return Response(content)    


class BusinessPlanQuestionsAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        data = json.loads(request.body)
        current_user = request.user
        for x, y in data.items():
            if x == 'BusinessPlanId':
                businessplanids = y
                user, planid = businessplanids.split('-')
                BPM = BusinessPlanModel.objects.filter(user = current_user.id).filter(planid = planid).first()
            elif x == 'Questions':
                for question in y:
                    question_model = Question.objects.filter(question=question['question']).first()
                    already_exsist = BusinessPlanQuestions.objects.filter(businessplanid=BPM).filter(question=question_model).first()
                    if already_exsist:
                        already_exsist.answer = question['answer']
                        already_exsist.save()
                    else: 
                        BPQ = BusinessPlanQuestions.objects.create(
                            businessplanid = BPM,
                            question = question_model,
                            answer = question['answer']
                        )
                        BPQ.save()
        content = {'message': 'Business Plan Questions Created Successfully'}

        return Response(content)  




# class userPlansQuestionsAPI(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request, format=None):
#         current_user = request.user

#         user_plans = [business_plan for business_plan in BusinessPlanModel.objects.all().filter(user = current_user.id).all()]
        
#         for plan in user_plans:
#             questions = BusinessPlanQuestions.objects.filter(businessplanid=plan).values().all()
#             print(questions)
#         content = {'message': 'Business Plan Questions Created Successfully'}

#         return Response(content) 