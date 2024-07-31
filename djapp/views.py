from django.shortcuts import render,redirect
from django.http import HttpResponse

from djapp.forms import StdForms
from .models import Std , Track
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StdSerializers

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
        

def cv(request):
	return render(request, 'djapp/cv.html')

# rest framework 
@api_view(['GET'])
def api(request):
    all_std = Std.objects.all()
    std_ser = StdSerializers(all_std , many= True)
    return Response(std_ser.data)

@api_view(['GET'])
def api_one(request ,std_id):
    api_st = Std.objects.get(id = std_id)
    std_ser = StdSerializers(api_st , many= False)
    return Response(std_ser.data)

@api_view(['POST'])
def api_add(request):
    api_add=  StdSerializers(data=request.data)
    if api_add.is_valid():
        api_add.save()
        return redirect('api')
    
@api_view(['POST'])
def api_edit (request , std_id):
    api_st = Std.objects.get(id = std_id)

    st_ser=  StdSerializers(data=request.data ,instance=api_st)
    if st_ser.is_valid():
        st_ser.save()
        return redirect('api')
     
@api_view(['DELETE'])
def api_del (request , std_id):
    d_st = Std.objects.get(id = std_id)
    d_st.delete()
    return  Response('Student Deleted Sucessfully  >> ')