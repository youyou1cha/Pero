from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase,override_settings
from django.urls import path

def response_error_handler(request,exception=None):
    return HttpResponse('Error handler content',status=403)

def permission_ddenied_view(request):
    raise PermissionDenied

urlpattern = [
    path('403/',permission_ddenied_view)
]

hanler403 = response_error_handler

from django.views.decorators.http import  require_http_methods,require_GET,require_POST,require_safe,condition

@require_http_methods(['GET','POST'])
def my_view(request):
    pass

# @condition()

from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def handle_uploaded_file(f):
    with open('some/file/name.txt','wb+') as d:
        for chunk in f.chunks():
            d.write(chunk)
from django.http import    HttpResponseRedirect

from django.shortcuts import render

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST):
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request,'upload.html',{'form':form})

# from .models import

from django.shortcuts import  get_list_or_404,get_object_or_404

def my_view(request):
    my_objects = get_list_or_404(mymodel,published=True)

from django.http import Http404

def my_view(request):
    my_objects = list(mymodel.objects.filter(published=True))
    if not my_objects:
        raise Http404('no my model matches the give query')

def my_1(request):
    obj = get_object_or_404(mymodel,pk=1)

def mm(request):
    try:
        obj = mmodel.objects.get(pk=1)

    except: mmodel.DoesNotExist:
        raise Http404('no')

from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse('Hello world')



from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = 'a'
        return context

from django.shortcuts import  get_object_or_404
from django.views.generic.base import RedirectView

class ArRedirectView(RedirectView):
    url = 'baidu.com'
    query_string = True
    permanent = False
    pattern_name = 'aaa'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args,**kwargs)

urlpattern = [
    path('mine/',MyView.as_view(),name='my-view'),
    path('',HomePageView.as_view(),name='home'),
    path('a/',ArRedirectView.as_view(),name='a')
]