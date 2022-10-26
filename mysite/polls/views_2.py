from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

from django.http import HttpResponseRedirect
from django.shortcuts import render


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(request,'name.html',{'form':form})

# <form>
#
# <>

from django.http import JsonResponse
from django.views.generic.edit import CreateView
from myapp.models import Author

