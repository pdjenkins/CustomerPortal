from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.urls import reverse
from django.conf import settings

# Create your models here.

class Product(models.Model):
    """Model representing Product Type"""
    name = models.CharField(max_length=200, help_text='Enter a Product Type (e.g. Fruit)')
	
    def __str__(self):
        """String for representing the Model object"""
        return self.name
	
    def get_absolute_url(self):
        """Returns the url to access a detail record for this product."""
        return reverse('product-detail', args=[str(self.id)])
		
class CustomUser(AbstractUser):
    pass
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address_text = models.CharField(max_length=200)
    bill_address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    CC_info = models.CharField(max_length=200, blank=True)
    save_CC = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'address_text', 'bill_address', 'save_CC']
    
    def __str__(self):
        return self.username
class Cart(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.owner.username + " cart"
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this cart."""
        return reverse('cart-detail', args=[str(self.id)])

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this Order')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	
    def __str__(self):
        """String for representing the Model object."""
        return self.owner.username + " order ID: " + str(self.id)
    def get_absolute_url(self):
        """Returns the url to access a detail record for this cart."""
        return reverse('order-detail', args=[str(self.id)])


class Item(models.Model):
    name = models.CharField(max_length=200)
    product_type = models.ManyToManyField('Product', help_text='Select a Product Type')
    price = models.DecimalField(max_digits=10 ,decimal_places=2, default=0.00)
    picture = models.ImageField(upload_to='images/', default='images/default.png')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this item."""
        return reverse('item-detail', args=[str(self.id)])
	
class ItemInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this Item')
    item = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.SET_NULL, null=True, blank=True)
    expirydate = models.DateField(null=True, blank=True)
	
    AVAILABILITY = (
    ('a','Available'),
    ('c', 'Cart'),
    ('o','Order'),
    )
    status = models.CharField(
        max_length=1,
        #choices=AVAILABILITY,
        blank=True,
        #default='a',
        help_text='Item availability',
    )
	
    def toOrder(Self, Order):
        self.order = Order.objects.get(id)
	
    def get_absolute_url(self):
        """Returns the url to access a detail record for this item."""
        return reverse('iteminstance-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.item.name})'
		
