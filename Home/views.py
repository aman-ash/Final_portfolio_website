from django.shortcuts import render
from Home.models import Contact

# Create your views here.


def Home(request):
    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['phone']
        desc = request.POST['message']
        #print(name, email, phone, desc)
        ins = Contact(name=name, number=number, email=email, desc=desc)
        ins.save()
        # print("the data has been written inside the database")

    return render(request, 'home.html')
