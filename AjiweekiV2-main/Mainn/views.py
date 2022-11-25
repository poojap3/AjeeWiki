from django.conf import settings
from django.db.models import base
from django.db.utils import IntegrityError
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
# from requests import api
from rest_framework.response import Response
from requests.api import head, request

from django.utils.decorators import method_decorator
# from accounts.decorator import *
import requests
import random
import json
import inspect
from django.core.mail import message, send_mail, EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.http import HttpResponsePermanentRedirect

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from .models import *
import jwt
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework import generics,viewsets, status
from django.contrib import auth
# from .serializers import *
from rest_framework import viewsets, status
# from accounts.backends import *
from rest_framework.authtoken.views import ObtainAuthToken
import time
import datetime
from django.db.models import Sum
import re


from django.views.decorators.csrf import csrf_exempt


# This class is used to create Form detail.

class FormAPIView(APIView):
    # def get(self, request):
    #     #breakpoint()
    #     id=self.request.query_params.get('id')
    #     #id = request.GET('name')
    #     print(id)
    #     print(2134567890)
    #     if id:
    #         appdata = Form.objects.filter(id=id).values('id','name','description')
    #         return Response(appdata)
    #     else:
    #         data = Form.objects.all().values()
    #         return Response(data)

    #this api for filter form name
    def get(self, request):
        #breakpoint()
        category_name=self.request.query_params.get('category_name')
        if category_name:
            appdata = Form.objects.filter(category_name=category_name).values('id','name','description','category_name')
            return Response(appdata)
        else:
            data = Form.objects.all().values()
            return Response(data)



    # def post(self, request):
    #     data = request.data
    #     # application_id=data.get('application_id')
    #     name = data.get('name')
    #     description = data.get('description')
    #     if data:
    #         obj=Form.objects.create(name=name, description=description)
    #         # return Response(response_result['result'])
    #         #var = int(Form.objects.latest('id').id)-1
    #         #return Response(int(Doctors.objects.latest('id').id)+1)
    #         response_result = {}
    #         response={}
    #         response_result['result'] = {
    #             'result':{'data':'Data added sucessfully',
    #             'form_id': Form.id,
    #             }}
    #         response['status'] = status.HTTP_200_OK
    #         return Response(response_result['result'],headers=response,status=status.HTTP_200_OK)

    #         #return Response({"Data For Application, Added Sucessfully"})
    #     else:
    #         return Response("Data Required For Application")




    def post(self, request):
        data = request.data
        # application_id=data.get('application_id')
        name = data.get('name')
        description = data.get('description')
        category_name = data.get('category_name')
        if Form.objects.filter(name=name).exists():
            return Response({'Error':{'Message':'Form Name Already Exist'}})
        else:
            var = Form.objects.create(name=name,description=description,category_name=category_name)
            response_result = {
                'result':{'data':'Data added sucessfully',
                'form_id':Form.id,
                'status':'HTTP_200_OK'
                }}
            #response['status'] = 'HTTP_200_OK'
            return Response(response_result['result'],status= status.HTTP_200_OK)

        # else:
        #    return Response("Data Required For Application")


    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = Form.objects.filter(id=id).update(name=data.get('name'), description= data.get('description'),category_name=data.get('category_name') )

            if data:
                    return JsonResponse({'Message': 'Data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'Id Required.'})


    def delete(self, request):


        id =self.request.query_params.get('id')
        item = Form.objects.filter(id= id)

        if len(item) > 0:
            item.delete()
            return Response("Data Deleted Sucessfully")
        else:
            return Response("Id Required.")



#class QuestionsAPIView(APIView):
    # CheckAuth(request)
    # def get(self, request):
    #     id =self.request.query_params.get('id')
    #     if id:
    #         appdata = Questions.objects.filter(id=id).values()
    #         return Response(appdata)
    #     else:
    #         appdata = Questions.objects.all().values()
    #         return Response(appdata)
    # To get the list of options


    # def get(self, request):
    #     #breakpoint()
    #     id =self.request.query_params.get('form_id')
    #     if id:
    #         appdata = Questions.objects.filter(form_id=id).values('id','form_id','form__name', 'is_required','question_type_id', 'question_type__name')

    #         appdata = list(appdata)
    #         for i in appdata:
    #             choice_obj = QuestionChoice.objects.filter(question_id=i['id']).values()
    #             print(choice_obj)
    #             i['options'] = []
    #             i['options'].append(choice_obj)
    #         #print(appdata)
    #         return Response(appdata)
    #     else:
    #         appdata = Questions.objects.all().values()
    #         return Response(appdata)



# This class is used to create Questions detail.

class QuestionsAPIView(APIView):
    def get(self, request):
        id =self.request.query_params.get('form_id')
        if id:
            appdata = Questions.objects.filter(form_id=id).values('id','form_id','form__name', 'name','elements','is_required','question_type_id', 'question_type__name')
            print(appdata)
            #my_list = list(elements.values())
            appdata = list(appdata)
            for i in appdata:
                choice_obj = QuestionChoice.objects.filter(question_id=i['id']).values()
                print(choice_obj)
                i['options'] = []
                i['options'].append(choice_obj)
            return Response(appdata)
        else:
            appdata = Questions.objects.all().values()
            return Response(appdata)


    def post(self, request):
        data = request.data
        # application_id=data.get('application_id')
        name = data.get('name')
        is_required = data.get('is_required')
        question_type= data.get('question_type_id')
        form_id = data.get('form_id')
        name=data.get('name')
        elements=data.get('elements')
        question_id=data.get('question_id')
        # option=data.get("QuestionChoice")
        questionchoice=data.get('questionchoice')
        if Questions.objects.filter(name=name).exists():
            return Response(({'Error':{'Message':'Question have Already Exist'}}))
        else:
            question = Questions.objects.create(name=name, is_required=is_required,question_type_id=question_type,form_id=form_id,elements=elements)
            if questionchoice is not None:
                for i in questionchoice:
                    # print("i",i)
                    option=QuestionChoice.objects.create(question_id=question.id,name=i['name'])
                response_result = {}
                response={}
                response_result['result'] = {
                'result':{'data':'Data added sucessfully',
                'form_id': form_id,
                'question_type_id':question_type,
                'name': name,
                'status':'HTTP_200_OK'
                }}
                #var = int(Questions.objects.latest('id').id)
                return Response(response_result['result'],headers=response,status= status.HTTP_200_OK)
            else:
                return Response(response_result['result'],headers=response,status= status.HTTP_200_OK)

    # def post(self, request):
    #     #breakpoint()
    #     data = request.data
    #     # application_id=data.get('application_id')
    #     name = data.get('name')
    #     is_required = data.get('is_required')
    #     question_type= data.get('question_type_id')
    #     form_id = data.get('form_id')
    #     name=data.get('name')
    #     elements=data.get('elements')
    #     question_id=data.get('question_id')
    #     # option=data.get("QuestionChoice")
    #     questionchoice=data.get('questionchoice')
    #     if data:
    #         vappcreate=Questions.objects.create(name=name, is_required=is_required,question_type_id=question_type,form_id=form_id,elements=elements)
    #         if questionchoice is not None:
    #             for i in questionchoice:
    #                 # print("i",i)
    #                 option=QuestionChoice.objects.create(question_id=vappcreate.id,name=i['name'])
    #         return Response("Data For Application, Added Sucessfully")
    #     else:
    #         return Response("Data Required For Application")


    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = Questions.objects.filter(id=id).update(name=data.get('name'), is_required= data.get('is_required'),
            question_type_id= data.get('question_type_id'),form_id= data.get('form_id'),elements=data.get("elements"))

            if data:
                    return JsonResponse({'message': 'data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'Id Required.'})

    def delete(self, request):
        id =self.request.query_params.get('id')
        item = Questions.objects.filter(id= id)
        if len(item) > 0:
            item.delete()
            return Response("data Deleted Sucessfully")
        else:
            return Response("Id Required.")


# This class is used to create UserResponse detail

class UserResponseAPIView(APIView):
    #CheckAuth(request)
    def get(self, request):
        id =self.request.query_params.get('id')
        if id:
            appdata = UserResponse.objects.filter(id=id).values()
            return Response(appdata)
        else:
            appdata = UserResponse.objects.all().values()
            return Response(appdata)


    def post(self, request):
        data = request.data
        # application_id=data.get('application_id')
        answer = data.get('answer')
        question_id = data.get('question_id')
        user_id = data.get('user_id')
        if data:
            vappcreate=UserResponse.objects.create(answer=answer, question_id=question_id,user_id=user_id)
            return Response("Data For Application, Added Sucessfully")
        else:
            return Response("Data Required For Application")


    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = UserResponse.objects.filter(id=id).update(answer=data.get('answer'),
            question_id= data.get('question_id'),user_id= data.get('user_id') )
            if data:
                    return JsonResponse({'message': 'data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'Id Required.'})



    def delete(self, request):
        id =self.request.query_params.get('id')
        item = UserResponse.objects.filter(id= id)
        if len(item) > 0:
            item.delete()
            return Response("data Deleted Sucessfully")
        else:
            return Response("Id Required.")


# This class is used to create QuestionChoice detail.

# class QuestionChoiceAPIView(APIView):
#     def get(self, request):
#         id =self.request.query_params.get('id')
#         if id:
#             appdata = QuestionChoice.objects.filter(id=id).values()
#             return Response(appdata)
#         else:
#             appdata = QuestionChoice.objects.all().values()
#             return Response(appdata)


#     def post(self, request):
#         data = request.data
#         # application_id=data.get('application_id')
#         name = data.get('name')
#         #elements = data.get('elements')
#         question_id = data.get('question_id')
#         if data:
#             vappcreate=QuestionChoice.objects.create(name=name,question_id=question_id)
#             return Response("Data For Application, Added Sucessfully")
#         else:
#             return Response("Data Required For Application")


#     def put(self, request):
#         data = request.data
#         id = data.get('id')
#         if id:
#             data = QuestionChoice.objects.filter(id=id).update(name=data.get('name'),  question_id= data.get('question_id') )
#             if data:
#                     return JsonResponse({'message': 'data Updated Sucessfully.'})
#             else:
#                 response={'message':"Invalid id"}
#                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return JsonResponse({'message': 'Id Required.'})


#     def delete(self, request):
#         id =self.request.query_params.get('id')
#         item = QuestionChoice.objects.filter(id= id)
#         QuestionChoice.objects.all().delete()

#         if len(item) > 0:
#             QuestionChoice.objects.all().delete()
#             # item.delete()
#             return Response("data Deleted Sucessfully")
#         else:
#             return Response("Id Required.")



# This is used to create UserwiseResponse Detail.

class UserwiseResponseAPIView(APIView):
    def post(self,request):
        data = request.data
        user_id = data.get("user_id")
        response = data.get("response")
        for i in response:
            print(i['question_id'])
            if i['answer'] == "others":
                response = UserResponse.objects.create(user_id=user_id,question_id=i['question_id'],answer=i['other_answer'])
                QuestionChoice.objects.create(question_id=i['question_id'],name=i['other_answer'])
            else:
                response = UserResponse.objects.create(user_id=user_id,question_id=i['question_id'],answer=i['answer'])
        return Response({"Data":"Data Created Successfully"})


# class QuestionanswerAPIView(APIView):
#     def get(self,request):
#         id = self.request.query_params.get('user_id')
#         if id:
#             data = UserResponse.objects.filter(id=id).values()
#             return Response(data)
#         else:
#             data = UserResponse.objects.filter().values()
#             return Response(data)


# This class is used to create QuestionAnswer Detail.
class QuestionanswerAPIView(APIView):
    def post(self,request):
        data = request.data
        question_id = data.get("question_id")
        #answer = data.get("answer")
        if data:
            obj= UserResponse.objects.filter(question_id=question_id).values('id','user_id','user__user_name','user__email','answer', 'question')
            # for i in obj:
            #     print(i)
            #     #print(i['answer'])
            #     #if i['answer'] == 'multiple_seclect':
            #     answers = UserResponse.objects.filter(question_id=i['id']).values()
            return Response(obj)
