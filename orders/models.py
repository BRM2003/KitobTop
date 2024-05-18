from django.db import models
from users.models import Users
from products.models import Books


class Baskets(models.Model):
    basket_id = models.CharField(max_length=256)
    client = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="client_basket")
    product = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='product_in_basket')
    added_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Baskets'
        verbose_name = 'Basket'

    def __str__(self):
        return self.basket_id


class Orders(models.Model):
    ORDER_OPEN = 1
    ORDER_PAYMENT = 2
    ORDER_ERROR = 3
    ORDER_SUCCESS = 4
    ORDER_CANCELED = 5
    ORDER_BLOCKED = 6

    ORDER_STATUS = [
        (ORDER_OPEN, 'Open'),
        (ORDER_PAYMENT, 'Execution of payment'),
        (ORDER_ERROR, 'Error'),
        (ORDER_SUCCESS, 'Success'),
        (ORDER_CANCELED, 'Canceled'),
        (ORDER_BLOCKED, 'Blocked'),
    ]

    order_id = models.CharField(max_length=64, primary_key=True)
    client = models.ForeignKey(Users, on_delete=models.DO_NOTHING, related_name='client')
    basket = models.ManyToManyField(Baskets)
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default=ORDER_OPEN)
    cipher = models.CharField(max_length=1024)
    amount = models.PositiveIntegerField()
    order_details = models.TextField()
    cr_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Orders'
        verbose_name = 'Order'

    def __str__(self):
        return self.order_id
