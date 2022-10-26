from django.urls import path,include
from . import views

extra_patterns = [
    path('reports/',views.DetailView),
    path('reposts/<int:id>',views.DetailView),
    path('charge/',views.DetailView)
]

urlpatterns = [
    path('',main_views.homepatge),
    path('help/',include('app.help.urls')),
    path('creite/',include(extra_patterns)),
]

urlpatterns1 = [
    path('aaaa/',include([
        path('history/',views.DetailView),
        path('edit/', views.DetailView),
        path('d/', views.DetailView),
        path('aa/', views.DetailView),
    ]))
]
