from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.

class IndexView(View):
    def __init__(self):
        super(IndexView, self).__init__()

    @classmethod
    def get(cls, request):
        context = {'user': None}
        return render(request, 'home/index.html', context=context)

class RegisterView(View):
    """docstring for RegisterView"""
    def __init__(self):
        super(RegisterView, self).__init__()
    
    def get(self, request):
        return HttpResponse('Success')
        