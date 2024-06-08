from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Std , Track


def home (request):
    # st = Std.objects.all()[0].fname
    # resp = "<h1> Wellcome Mr " + st + "</h1>"
    # return HttpResponse (resp)
    all_st = Std.objects.all()
    context = {'students':  all_st}
    return  render ( request ,  'djapp/home.html' ,context)


def main (request): 
    tr = Track.objects.all()[0].tname
    resp = "<h1> trak name is " + tr + "</h1> "
    return HttpResponse (resp)

def std_detail(request , std_id):
    st = Std.objects.get(id = std_id)
    context = {'student_details' : st}
    return render(request , 'djapp/details.html',context)


def delete (request , std_id):
    d_st = Std.objects.get(id = std_id)
    d_st.delete()
    return  redirect('home')