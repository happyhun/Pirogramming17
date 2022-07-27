from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def main(request):
    return render(request, 'pirostagram.html')

@csrf_exempt
def like_ajax(request):
    return JsonResponse({})
