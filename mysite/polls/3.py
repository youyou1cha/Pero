from django.contrib.auth import authenticate

user = authenticate(username='john',password='secret')
if user is not None:
    #
else:
    #

from django.views.generic import ListView
from myapp.models import Contact

class ContactListView(ListView):
    paginate_by = 2
    model = Contact

# 函数
from django.core.paginator import Paginator
from django.shortcuts import render

from myapp.Models import Contact

def listing(request):

    contact_all_list = Contact.object.all()
    paginator = Paginator(contact_all_list,25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return  render(request,'list.html',{'page_obj':page_obj})