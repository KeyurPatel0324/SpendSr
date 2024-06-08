from django.shortcuts import render,HttpResponse
from django.views import View
from .models import *
from django.db import connection
# Create your views here.

class ExpenseDetails(View):

    def get(self,request):
        try:
            query_data = list(expensemaster.objects.all().values())
            context = {"data":query_data}
            return render(request,'expense_view.html',context)
        except Exception as e:
            HttpResponse("Error is FilterExpenseData {}".format(e))

