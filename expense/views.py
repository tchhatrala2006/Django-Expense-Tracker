from django.shortcuts import render
from django.http import HttpResponse
from .import models
from django.shortcuts import redirect
def home(r):
    return render(r,'home.html')

def insert(r):
    if r.method=='POST':
        month=r.POST.get('month')
        name=r.POST.get('name')
        amount=r.POST.get('amount')
        date=r.POST.get('date')
        if not name=='' and not amount=='' and not date=='' and month=='January' or month=='February' or month == 'March' or month == 'April' or month == 'May' or month == 'June' or month == 'July' or month == 'August' or month == 'September' or month == 'October' or month == 'November' or month == 'December'   :
            a=models.et.objects.create(
                months=month,
                name=name,
                amount=amount,
                date=date
            )


            return redirect('show')
        return HttpResponse("Enter the Values in Fields")

def show(r):
    a=models.et.objects.filter(months='January')
    a1=models.et.objects.all()
    s=0
    for i in a.values():
        s+=i['amount']

    # for i in a:
    #     print(i)
    context={
       
        "a1":a1
    }
    # return HttpResponse(s)
    return render(r,'show.html',context)

def search(r):
    if r.method=='POST':
        month=r.POST.get('month')
        a=models.et.objects.filter(months=month)
        if a:
            s=0
            for i in a.values():
                s+=i['amount']

            context={
                "month":i['months'],
                'TotalExpense':s
            }
            return render(r,'search.html',context)
        else:
             return HttpResponse("Does Not Found Data")

def update(r,id):
    a=models.et.objects.get(id=id)
    context={
        "a":a
    }
    return render(r,'update.html',context)
def updated(r,id):
    a=models.et.objects.get(id=id)
    if r.method=='POST':
                month=r.POST.get('month')
                name=r.POST.get('name')
                amount=r.POST.get('amount')
                date=r.POST.get('date')
                if not name=='' and not amount=='' and not date=='' and month=='January' or month=='February' or month == 'March' or month == 'April' or month == 'May' or month == 'June' or month == 'July' or month == 'August' or month == 'September' or month == 'October' or month == 'November' or month == 'December'   :
                    
                        a.months=month
                        a.name=name
                        a.amount=amount
                        a.date=date
                        a.save()
                    
        
        
                        return redirect('show')
                return HttpResponse("Enter the Values in Fields")

def delete(r,id):
     a=models.et.objects.get(id=id)
     a.delete()
     return redirect('show')



    

        
