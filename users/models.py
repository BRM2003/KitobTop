from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='client')
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=32, unique=True)
    photo = models.ImageField(upload_to='users', null=True, blank=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    up_on = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        verbose_name_plural = 'Clients'
        verbose_name = 'Client'

    def __str__(self):
        return self.user.username


class Admins(models.Model):
    ADMIN_MANAGER = 'M'
    ADMIN_TOP_MANAGER = 'T'
    ADMIN_DIRECTOR = 'D'

    ADMIN_CHOICES = [
        (ADMIN_MANAGER, 'Manager'),
        (ADMIN_TOP_MANAGER, 'Top_manager'),
        (ADMIN_DIRECTOR, 'Director'),
    ]

    user = models.ForeignKey(Users, on_delete=models.PROTECT, related_name='User')
    membership = models.CharField(max_length=1, choices=ADMIN_CHOICES, default=ADMIN_MANAGER)
    cr_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='admin_created_by')
    up_by = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='admin_updated_by')
    cr_on = models.DateTimeField(auto_now_add=True)
    up_on = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        verbose_name_plural = 'Admins'
        verbose_name = 'Admin'

    def __str__(self):
        return "Admin: " + self.user.user.username


class Merchants(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    merchant_name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='Merchants', null=True, blank=True)
    address = models.CharField(max_length=1024)
    open_time = models.TimeField(null=True, blank=True)
    close_time = models.TimeField(null=True, blank=True)
    cr_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='merchant_created_by')
    up_by = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='merchant_updated_by')
    cr_on = models.DateTimeField(auto_now_add=True)
    up_on = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        verbose_name_plural = 'Merchants'
        verbose_name = 'Merchant'

    def __str__(self):
        return self.merchant_name

