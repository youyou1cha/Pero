from django.shortcuts import render
from django.http import HttpResponse, Http404, StreamingHttpResponse, FileResponse
import os


# Create your views here.

def file_download(request, file_path):
    # do something...
    with open(file_path) as f:
        c = f.read()
    return HttpResponse(c)


def media_file_download(request, file_path):
    with open(file_path, 'rb') as f:
        try:
            response = HttpResponse(f)
            response['content_type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
        except Exception:
            raise Http404


def file_response_download1(request, file_path):
    try:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    except Exception:
        raise Http404


def file_response_download(request, file_path):
    print(file_path)
    ext = os.path.basename(file_path).split('.')[-1].lower()

    if ext not in ['py', 'db', 'sqlite3']:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        raise Http404
