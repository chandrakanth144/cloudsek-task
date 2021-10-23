import django
django.setup()
from django.http.response import HttpResponse, Http404
import time
from .models import *
from multiprocessing import Process


def calculate_answer(identifier,num1,num2):
    time.sleep(10)
    ans = num1 + num2
    cal_answer = calculate.objects.get(id=identifier)
    cal_answer.answer = ans
    cal_answer.save()




# Create your views here.

def home(request):
    if request.method =='GET':
        return HttpResponse('<h1>Hi from test API</h1>',status=200)


def calculate_id(request,num1=None,num2=None):
    if request.method =='GET':
        answer = calculate(number1=num1,number2=num2)
        answer.save()
        last_ans =list(calculate.objects.filter(number1=num1,number2=num2).values('id'))
        ans = last_ans[0]['id']
        p = Process(target=calculate_answer, args=(ans,num1,num2))
        p.start()
        msg = f'The unique identifier for the request is {ans}'
        return HttpResponse(msg,status=200)

def get_answer(request,identifier=None):
    last_ans =list(calculate.objects.filter(id=identifier).values('answer'))
    if last_ans!= []:
        if last_ans[0]['answer'] !=None:
            ans = last_ans[0]['answer']
            msg = f'Answer = {ans}'
            return  HttpResponse(msg,status=200)
        else:
            msg = f'Please Wait'
            return HttpResponse(msg,status=200)
    else:
        raise Http404()


