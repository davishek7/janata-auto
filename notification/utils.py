from .models import Notification


def create_notification_on_asset_less_than_equal_to_five(instance, count):

    notification = Notification.objects.create(
                title = f'{instance} is about end.',
                content = f'{instance} left only {count}.',
                type = Notification.WARNING
                )