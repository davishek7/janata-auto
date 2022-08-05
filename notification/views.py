from django.shortcuts import render, redirect
from .models import Notification

# Create your views here.

def notification_list(request):
    notifications = Notification.objects.filter(status = True)
    notifications.update(read_status = True)
    context = {'notifications':notifications}
    return render(request, 'notification/list.html', context=context)

def create_notification(request):
    context = {}
    return render(request, 'notification/create.html',context=context)