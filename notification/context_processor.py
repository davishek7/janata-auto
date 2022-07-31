from .models import Notification

def notification_list(request):

    return{
        'notifications_navbar' : Notification.objects.filter(status=True)[:5],
        'notification_count' : Notification.objects.filter(read_status=False).count()
    }