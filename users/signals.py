from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


from .models import MyUser


# @receiver(post_save, sender=User)
# def create_a_user(sender, instance, created, **kwargs):
#     if created:
#         MyUser.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def update_a_user(sender, instance, **kwargs):
#     instance.myuser.save()


''' My Notes: 

    in order to make the signals works 
    >>> 1) add the following code in the 'apps.py' as a method in the 'UsersConfig' class
        
        def ready(self):
            import main_app.signals
            
            
    >>> 2) and add the following line of code in the '__init__.py' file
    
    default_app_config = 'users.apps.UsersConfig'
'''