from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')

    def post(self, request):
        return render((request, 'home/home.html'))
