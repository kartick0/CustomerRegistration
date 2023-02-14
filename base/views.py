from django.shortcuts import render
from .forms import CustomerRegistrationForm
# Create your views here.

def home(request):
    if request.method=='POST':
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            name=form.cleaned_data['cname']            
            age=form.cleaned_data['age']            
            address=form.cleaned_data['address']            
            phoneNumber=form.cleaned_data['phoneNumber']            
            email=form.cleaned_data['email']            

            context={
                'name':name,
                'age':age,
                'address':address,
                'phoneNumber':phoneNumber,
                'email':email
            }

            return render(request,'customerdetails.html',context )
        else:
            err=form.errors
            # form=CustomerRegistrationForm()
            
            # return render(request,'home.html', {'form':form, 'err':err})
    else:
        form=CustomerRegistrationForm()

    return render(request,'home.html', {'form':form})