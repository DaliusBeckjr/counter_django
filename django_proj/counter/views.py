from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
# Create your views here.
def index (request):

    if 'visits' in request.session:
        print('key exist!!!!')
        request.session['visits'] += 1
    else:
        print('key does NOT exist!!!!!')
        request.session['visits'] = 0


    return render(request, 'index.html')


def add_one (request):
    request.session['visits'] += 1
    return redirect('/')


def destroy_session (request):
    del request.session['visits']
    return redirect('/')