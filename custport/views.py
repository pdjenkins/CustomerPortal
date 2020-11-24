from django.shortcuts import render

# Create your views here.

from django import forms
from django.core.exceptions import ValidationError
from custport.models import Product, Item, CustomUser, ItemInstance, Order, Cart
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.http import Http404

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    items_instance_list = ItemInstance.objects.filter(status__contains='a')
    items_instance_num = ItemInstance.objects.filter(status__contains='a').count()
	
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'items_instance_list': items_instance_list,
        'items_instance_num': items_instance_num,
		'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class ItemListView(generic.ListView):
    model = Item
	
class ItemDetailView(generic.DetailView):
    model = Item
	
class ProductListView(generic.ListView):
    model = Product
	
class ProductDetailView(generic.DetailView):
    model = Product
	
class ItemInstanceDetailView(generic.DetailView):
    model = ItemInstance

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
class CartView(generic.ListView):
    model = Cart
#def addToCart(request, itemid, user):
def addToCart(request, itemid, user):
    try:
        item = ItemInstance.objects.get(id=itemid)
        #cart = Cart.objects.get(owner=user)
        #cart.add_item(item)
    except ItemInstance.DoesNotExist:
        raise Http404("Item does not exist")
    #except Cart.DoesNotExist:
    #    raise Http404("Cart does not exist or user does not exist")
    
    # Generate counts of some of the main objects
    items_instance_list = ItemInstance.objects.filter(status__contains='a')
    items_instance_num = ItemInstance.objects.filter(status__contains='a').count()
	
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'items_instance_list': items_instance_list,
        'items_instance_num': items_instance_num,
		'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)
