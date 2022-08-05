from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BatterySale, EngineOilSale, DistilledWaterSale, ScrapBatterySale, InverterSale
from asset.models import Battery, Inverter, EngineOil, DistilledWater
from datetime import timedelta
from django.utils import timezone
from django_q.tasks import schedule
from django_q.models import Schedule


@receiver(post_save, sender=BatterySale)
def change_battery_status_and_create_record(sender, created, instance, **kwargs):
    if created:
        asset = Battery.objects.filter(id = instance.battery.id, status=True).first()
        asset.status = False
        asset.save()

@receiver(post_save, sender=EngineOilSale)
def change_engine_oil_quantity(sender, created, instance, **kwargs):
    if created:
        asset = EngineOil.objects.filter(id = instance.engine_oil.id, status=True).first()
        asset.quantity -= 1
        asset.save()

        if asset.quantity == 5:
            schedule(
                'notification.utils.create_notification_on_asset_equal_to_five',
                asset.product.name,
                f'{asset.product.size.size} ml',
                asset.quantity,
                schedule_type=Schedule.ONCE,
                next_run=timezone.now() + timedelta(seconds=10)
            )

@receiver(post_save, sender=DistilledWaterSale)
def change_distilled_water_quantity(sender, created, instance, **kwargs):
    if created:
        asset = DistilledWater.objects.filter(id = instance.distilled_water.id, status=True).first()
        asset.quantity -= 1
        asset.save()

        if asset.quantity == 5:
            schedule(
                'notification.utils.create_notification_on_asset_equal_to_five',
                asset.product.name,
                f'{asset.product.size.size} ltr',
                asset.quantity,
                schedule_type=Schedule.ONCE,
                next_run=timezone.now() + timedelta(seconds=10)
            )

@receiver(post_save, sender=InverterSale)
def change_inverter_status_and_create_record(sender, created, instance, **kwargs):
    if created:
        asset = Inverter.objects.filter(id = instance.inverter.id, status=True).first()
        asset.status = False
        asset.save()

    # if instance_asset.quantity <= 5:
