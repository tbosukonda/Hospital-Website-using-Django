from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import DoctorModel,CustomerModel,BookapptModel
# Create your views here.


def adminloginview(request):
    return render(request, "adminlogin.html")

def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username, password = password)

    #if user exists
    if user is not None and user.username=="admin":
        login(request,user)
        return redirect('adminhomepage')
    #user doesn't exists
    if user is None:
        messages.add_message(request,messages.ERROR,"Invalid Credentials")
        return redirect('adminloginpage')

def adminhomepageview(request):
    context = {'doctors': DoctorModel.objects.all()}
    return render(request,"adminhomepage.html",context)

def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')

def adddoctor(request):
    name = request.POST['doctor']
    speciality = request.POST['speciality']
    schedule = request.POST['schedule']
    DoctorModel(name = name, speciality=speciality, schedule = schedule).save()
    return redirect('adminhomepage')

def deletedoctor(request, doctorpk):
    DoctorModel.objects.filter(id = doctorpk).delete()
    return redirect('adminhomepage')

def homepageview(request):
    return render(request,"homepage.html")

def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    contactno = request.POST['contactno']

    if User.objects.filter(username = username).exists():
        messages.add_message(request, messages.ERROR, "USER ALREADY EXISTS!!")
        return redirect('homepage')
    User.objects.create_user(username=username, password=password).save()
    lastobject = len(User.objects.all())-1
    CustomerModel(id = User.objects.all()[int(lastobject)].id, contactno = contactno).save()
    messages.add_message(request, messages.ERROR, "USER SUCCESSFULLY CREATED!!")
    return redirect('homepage')

def userloginview(request):
    return render(request,"userlogin.html")

def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect('customerpage')
    #user doesn't exists
    if user is None:
        messages.add_message(request,messages.ERROR,"Invalid Credentials")
        return redirect('userloginpage')

def customerwelcomeview(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')
    username = request.user.username
    context = {'username':username, 'doctors': DoctorModel.objects.all()}
    return render(request,'customerwelcome.html',context)

def userlogout(request):
    logout(request)
    return redirect('userloginpage')

def bookappt(request,doctorpk):
    username = request.user.username
    contactno = CustomerModel.objects.filter(id=request.user.id)[0].contactno
    name = ""
    speciality = ""
    schedule = ""
    book = doctorpk
    for d in DoctorModel.objects.filter(id=book):
        name = name + d.name
        speciality = speciality + d.speciality
        schedule = schedule + d.schedule

    BookapptModel(username=username, contactno=contactno, name=name, speciality=speciality, schedule=schedule).save()
    messages.add_message(request, messages.ERROR, "Appointment scheduled")
    """for doctor in DoctorModel.objects.all():
        book = DoctorModel.objects.filter(id=request.POST.get(doctor.id))
        for i in book[0]:
            print(i)
        if book.id==" ":
            continue
        print(book)
        for d in DoctorModel.objects.filter(id=book):
            name = name+d.name
            speciality = speciality+d.speciality
            schedule = schedule+d.schedule

    BookapptModel(username= username, contactno= contactno, name = name, speciality=speciality, schedule = schedule).save()
    messages.add_message(request, messages.ERROR, "Appointment scheduled")"""
    return redirect('customerpage')

def userappt(request):
    appt = BookapptModel.objects.filter(username = request.user.username)
    context = {'appts' : appt}
    return render(request,'userappt.html',context)

def adminappts(request):
    appts = BookapptModel.objects.all()
    context = {'appts' : appts}
    return render(request, 'adminappts.html', context)

def acceptappt(request, apptpk):
    appt = BookapptModel.objects.filter(id=apptpk)[0]
    appt.status="ACCEPTED"
    appt.save()
    return redirect(request.META['HTTP_REFERER'])
def declineappt(request, apptpk):
    appt = BookapptModel.objects.filter(id=apptpk)[0]
    appt.status = "DECLINED"
    appt.save()
    return redirect(request.META['HTTP_REFERER'])
