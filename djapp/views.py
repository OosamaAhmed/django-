from django.shortcuts import render,redirect
from django.http import HttpResponse

from djapp.forms import StdForms
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

#  delete element-------------------------------> 
def delete (request , std_id):
    d_st = Std.objects.get(id = std_id)
    d_st.delete()
    return  redirect('home')

# create new element-------------------------------> 
def add(request): 
    if request.method== 'POST':
        st_form=  StdForms(request.POST)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    else: 
            
        st_form= StdForms()
        context = {'form' : st_form}
        return render(request , 'djapp/add.html',context)
    

# Edit  element-------------------------------> 

def edit(request ,std_id):  
    st = Std.objects.get(id = std_id)

    if request.method== 'POST':
        st_form=  StdForms(request.POST ,instance=st)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    else: 
        form = StdForms(instance=st)
        context = {'form' : form} 
        # the same name to render on add form
        return render(request , 'djapp/add.html',context)
        