from django.shortcuts import render
from django.views.generic import View


class MainView (View):

    def get (self, request, params=None):
        return render(request, 'main_view.html')
