from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.db.models.signals import post_save



class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomerModel(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    last_seen = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
    def update_last_seen(self):
        self.last_seen = timezone.now()
        self.save(update_fields=['last_seen'])

class CustomerProfileModel(models.Model):
    user=models.OneToOneField(CustomerModel,on_delete=models.CASCADE,related_name="profile")
    city=models.CharField(max_length=100,blank=True)
    profile_pic = models.ImageField(upload_to='profile_img',null=True,blank=True)
    
    def __str__(self):
        return str(self.user.first_name)


def create_profile(sender, created, instance, **kwargs):
    if created:
        CustomerProfileModel.objects.create(user=instance)
post_save.connect(create_profile, sender=CustomerModel)

def update_last_seen(sender, request, user, **kwargs):
    user.update_last_seen()


