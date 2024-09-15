from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from apps.users.models import *



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        ActionLog.objects.create(user=instance, action="Foydalanuvchi yaratildi")



@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    ActionLog.objects.create(user=instance, action='Foydalanuvchi ma`lumotlari yangilandi')


@receiver(pre_delete, sender=CustomUser)
def user_deletion(sender, instance, **kwargs):
    ActionLog.objects.create(user=instance, action='Foydalanuvchi o`chirildi')