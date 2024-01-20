from django.shortcuts import render
from django.http import HttpResponse
from .models import Input
from django.utils import timezone



def home(request):
    return render(request, 'base.html')



def result(request):

    num1 = int(request.GET.get('number1'))
    num2 = int(request.GET.get('number2'))

    # add data to database and operations
    addEntry(num1, num2)

    if request.GET.get('alldata') == "":
     #return array of data
        entryList = getEntries()
        return render(request, 'resultlist.html', {'list': entryList})
    else:
        #return answer
        ANS = operations(num1, num2, request)
        return render(request, 'result.html', {'ans': ANS})
    



# Return calculations 
def operations(num1, num2, request):
     
     if request.GET.get('add') == "":
        ans = num1 + num2     
     elif request.GET.get('subtract') == "":
        ans = num1 - num2
     elif request.GET.get('multiply') == "":
        ans = num1 * num2
     elif request.GET.get('divide') == "":
         ans = num1 / num2
     else:
        ans = (num1 + num2)/2

     return ans   



# Collect/Display all entries
def getEntries():
   
   allVal =  Input.objects.all().values()   
   list = []
   return allVal 



# Adds entry to database
def addEntry(num1, num2):

    Input.objects.create(input_a = num1, input_b = num2, pub_date = timezone.now())
    return


