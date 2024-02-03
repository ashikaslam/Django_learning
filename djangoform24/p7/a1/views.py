from django.shortcuts import render,redirect
from .import forms
from . import models
# Create your views here.
def home(request):
    if request.method == 'POST':
        print(100002)
        form = forms.Stufrom(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(10000)
            form.save(commit=True)





    fom = forms.Stufrom
    return render(request,'home.html',{'form':fom})


# for many to many 

def show_stu_for_tec(request,name_of_tc):
    current_teacher = models.Tec.objects.get(name = name_of_tc)
   
  #  st_list = current_teacher.stu_List()# with class name
    st_list = current_teacher.stuednts.all() # with atribute name
    if st_list:
        for i in  st_list:print(i,10)
    else :print(404)

    return render(request,'stu_for_tec.html')



def show_tec(request):
    st = models.Stu.objects.get(name='a')
    tecc = st.teachers.all()  
  #  tecc = st.tec_set.all() # tec is the name of calss in lower case 
    if tecc:
        for i in tecc:print(i)
    else :print(404)
    return render(request,'stu_for_tec.html')



# for one to one


def people_with_passport(request):
    passPOrt = models.Passport.objects.get(pk = 1)
    print(passPOrt.total_page,200)
    uere = passPOrt.user_id
    print(uere,uere.age)
    print('howw')
    return render(request,'stu_for_tec.html')


def passport_with_people(request):
    people = models.People.objects.get(name = 'aslam')
    
    passs =  people.pas
    print(passs.total_page)
    
    return render(request,'stu_for_tec.html')
