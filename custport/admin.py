from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Product, Item, ItemInstance, Order

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'address_text', 'bill_address', 'CC_info','save_CC']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product)
admin.site.register(Item)
admin.site.register(ItemInstance)
admin.site.register(Order)