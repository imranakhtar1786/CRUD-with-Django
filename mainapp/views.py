from django.shortcuts import render,redirect
from mainapp.models import employee
from django.db.models import Q
def mainApp(Request):
    emp=employee.objects.all()
    return render(Request,"index.html",{'data':emp})
def Add(Request):
    if Request.method == "POST":
        name=Request.POST.get("name")
        email=Request.POST.get("email")
        phone=Request.POST.get("phone")
        des=Request.POST.get("Designation")
        salery=Request.POST.get("salery")
        city=Request.POST.get("City")
        state=Request.POST.get("State")
        emp=employee(
            name=name,
            email=email,
            phone=phone,
            dsg=des,
            salery=salery,
            city=city,
            state=state
        )
        emp.save()
        return redirect("/")

    return render(Request,"add.html")
def deleteRecord(Request,id):
    try:
        data=employee.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect("/")
def UpdateRecord(Request,id):
    try:
        data=employee.objects.get(id=id)
        if Request.method=="POST":
            data.name=Request.POST.get("name")
            data.email=Request.POST.get("email")
            data.phone=Request.POST.get("phone")
            data.dsg=Request.POST.get("Designation")
            data.salery=Request.POST.get("salery")
            data.city=Request.POST.get("City")
            data.state=Request.POST.get("State")
            data.save()
            return redirect("/")
        return render(Request,"edit.html",{'data':data})
    except:
        pass
    return redirect("/")
def searchPage(Request):
    if(Request.method == "POST"):
        search=Request.POST.get("search")
        data = employee.objects.filter(Q(name__icontains=search) | Q(city__icontains=search) |Q(state__icontains=search) |Q(email__icontains=search)|Q(phone__icontains=search)|Q(dsg__icontains=search))
        return render(Request,"index.html",{'data':data})
    else:
        return redirect("/")
