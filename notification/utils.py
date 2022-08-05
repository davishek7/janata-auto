from .models import Notification


def create_notification_on_asset_equal_to_five(name, size, quantity):

    Notification.objects.create(
        title = f'{size} {name} is about to end.',
        content = f'{size} {name} is only {quantity} left.',
        type = Notification.WARNING
    )