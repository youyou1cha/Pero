from django.shortcuts import render, redirect
from .models import File
from .forms import FileUploadForm, FileUploadModelForm
import os
import uuid
from django.http import JsonResponse
from django.template.defaultfilters import filesizeformat


# Create your views here.

def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_method = form.cleaned_data.get('upload_method')
            raw_file = form.cleaned_data.get('file')
            new_file = File()
            new_file.file = handle_uploaded_file(raw_file)
            new_file.upload_method = upload_method
            new_file.save()
            return redirect('/file/')
    else:
        form = FileUploadForm()
    return render(request, 'file_upload/upload_form.html', {'form': form, 'heading': 'Upload files with Regular Form'})


def handle_uploaded_file(file):
    ext = file.name.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    file_path = os.path.join('files', file_name)
    absolute_file_path = os.path.join('media', 'files', file_name)

    directory = os.path.dirname(absolute_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(absolute_file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return file_path


def model_form_upload(request):
    if request.method == 'POST':
        form = FileUploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/file/')
    else:
        form = FileUploadModelForm()
    return render(request, 'file_upload/upload_form.html', {'form': form, 'heading': 'Upload files with ModelForm', })


def ajax_form_upload(request):
    form = FileUploadModelForm()
    return render(request, 'file_upload/ajax_upload_form.html', {'form': form, 'heading': 'File Upload with ajax'})


def ajax_upload(request):
    if request.method == 'POST':
        # 1
        upload_method = request.POST.get('upload_method')
        raw_file = request.FILES.get('file')
        new_file = File()
        new_file.file = handle_uploaded_file(raw_file)
        new_file.upload_method = upload_method
        new_file.save()

        # 2
        form = FileUploadModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            files = File.objects.all().order_by('-id')
            data = []
            for file in files:
                data.append(
                    {'url': file.file.url,
                     "size": filesizeformat(file.file.size),
                     "upload_method": file.upload_method, }
                )
            return JsonResponse(data, safe=False)
        else:
            data = {'error_msg': 'only jpq,pdf and xlsx files are allowed'}
            return JsonResponse(data)
    return JsonResponse({'error_msg': 'only POST method accpeted'})


def file_list(request):
    files = File.objects.all().order_by('-id')
    return render(request, 'file_upload/file_list.html', {'files': files, })
