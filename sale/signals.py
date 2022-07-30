from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Sale
from asset.models import Battery, Inverter, EngineOil, DistilledWater
from datetime import timedelta
from django.utils import timezone
from django_q.tasks import schedule
from django_q.models import Schedule


@receiver(post_save, sender=Sale)
def change_asset_status_and_quantity_on_sale(sender, created, instance, **kwargs):
    if created:
        instance_asset = None
        if instance.category.name == "Battery":
            instance_asset = Battery.objects.filter(serial_no = instance.serial_no).first()
            instance_asset.status = False
            instance_asset.save()

        elif instance.category.name == "Inverter":
            instance_asset = Inverter.objects.filter(serial_no = instance.serial_no).first()
            instance_asset.status = False
            instance_asset.save()

        elif instance.category.name == "Engine Oil":
            instance_asset = EngineOil.objects.filter(product = instance.product).first()
            instance_asset.quantity -= 1
            instance_asset.save()

        elif instance.category.name == "Distilled Water":
            instance_asset = DistilledWater.objects.filter(product = instance.product).first()
            instance_asset.quantity -= 1
            instance_asset.save()