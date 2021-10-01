from django.shortcuts import render,HttpResponse
from app.models import Contact
# Create your views here.
def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(name,email,message)
        ins = Contact(Name=name,Email=email,Message=message)
        ins.save()
        print("the data has submitted")
    #return HttpResponse("this is contact page (/contact)")
    return render(request,'contactus.html')