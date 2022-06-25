from django.shortcuts import render

# Create your views here.

def notification_list(request):
    return render(request, 'notification/list.html')