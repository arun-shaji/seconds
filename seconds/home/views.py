from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.

class IndexView(View):
    def __init__(self):
        super(IndexView, self).__init__()

    @classmethod
    def get(cls, request):
        return render(request, 'home/index.html', context={})
