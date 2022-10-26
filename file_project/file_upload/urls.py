from django.urls import re_path,path
from . import views

app_name = 'file_upload'

urlpatterns = [
    re_path(r'^upload1/$',views.file_upload,name='file_upload'),
    re_path(r'^upload2/$',views.model_form_upload,name='model_form_upload'),
    re_path(r'^upload3/$',views.ajax_form_upload,name='ajax_form_upload'),
    re_path(r'^ajax_upload/$',views.ajax_upload,name='ajax_upload'),
    # re_path(r'^/$',views.file_list,name='file_list'),
    path('',views.file_list,name='file_list'),
]