from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
from pagos.models import Pagos
from django.contrib.auth.models import AbstractUser


class Services(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Name = models.ForeignKey(Pagos,on_delete=models.CASCADE,related_name="servicios")
    Description = models.TextField(max_length=150)
    Logo = models.URLField(max_length=70)
    
class Payment_user(models.Model):
    Id = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete =models.CASCADE, related_name='versionedPagos')
    Service_id = models.ForeignKey(Services, on_delete =models.CASCADE, related_name='versionedPagos')
    Amount = models.IntegerField(max_length=7)
    PaymentDate = models.DateField(auto_now=False,auto_now_add=True)
    ExpirationDate = models.DateField(auto_now_add=True)

class Expired_payments(models.Model):
    Id =models.BigAutoField(primary_key=True)
    Payment_user_id = models.ForeignKey(Payment_user,on_delete=models.CASCADE,related_name="PaymentDate")
    Penalty_fee_amount = models.IntegerField(default=0.0)

class Userversioned(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=80, unique=True, default="none@email.com")
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)