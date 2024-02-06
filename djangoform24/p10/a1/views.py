from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime,timedelta

# Create your views here.


def home(request):
    response =  render(request,'home.html')
   # response .set_cookie('name','aslam1111',max_age=10)
    response .set_cookie('name','aslam1111',expires=datetime.utcnow()+timedelta(days=7))
   ## response .set_cookie('name','xt')
    name = request.COOKIES.get('name')
    print(name)
    
    return response


def del_cpy(request):
     response =  render(request,'home.html')
     response.delete_cookie('name')
     return response



def set_sesson(request):
    data = {'name': 'aslam', 'age': 20, 'lan': 'bn'}
    request.session.update(data)

    # Get session data from the backend database
    all_data = request.session
    print("Session data:", all_data)

    # Iterating over session items
    for key, value in all_data.items():
        print(f"{key}: {value}, Type: {type(value)}")
    
    amar_nam = request.session.get('name')
    ageee = all_data.get('age')
    print(amar_nam,ageee)
    time_to_stay   = request.session.get_session_cookie_age()
    xyz = request.session.get_expiry_date()
    print("total ato din tahkbe ",time_to_stay)
    # del request.session['name'] # to del perticula field
    #request.session.flush() # to dell all for the user
    # print('after>> del>>')
    # for key, value in all_data.items():
    #     print(f"{key}: {value}, Type: {type(value)}")
    response = render(request, 'home.html')
    return response



def del_seesson(request):
    pass # i did it the set_fun








def get_ssseess(request):
    time_to_stay   = request.session.get_session_cookie_age()
    xyz = request.session.get_expiry_date()
    print("total ato din tahkbe ",time_to_stay)
    all_data = request.session
    print("Session data:", all_data)
    request.session.modified = True
    # Iterating over session items
    for key, value in all_data.items():
        print(f"{key}: {value}, Type: {type(value)}")
    
    if 'name' in request.session:return render(request,'see.html',{'nam':request.session['name']})
    else :return HttpResponse("sorry no data")














