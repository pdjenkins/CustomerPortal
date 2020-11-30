from django.shortcuts import render
from django.db.models import Q

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
from django.db import models

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

class SearchResultsView(generic.ListView):
    model = Item
    template_name = 'search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Item.objects.filter(Q(name__icontains=query))
        return object_list 
	
class ProductDetailView(generic.DetailView):
    model = Product
	
class ItemInstanceDetailView(generic.DetailView):
    model = ItemInstance

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
class CartView(generic.DetailView):
    model = Cart

def addToCart(request, itemid):
    try:
        item = ItemInstance.objects.get(id=itemid)
        current_user = CustomUser.objects.get(username=request.user)
        cart = Cart.objects.get(owner=request.user)
        #set item status
        item.status = 'c'
        item.save(update_fields=["status"])
        #add the item to the cart by setting its foreign key to this cart object
        cart.iteminstance_set.add(item)
        cart.save()
    except ItemInstance.DoesNotExist:
        raise Http404("Item does not exist")
    except Cart.DoesNotExist:
        #create the cart
        cart = Cart(owner=request.user)
        #save it to the database
        cart.save()

    #This handles the user not being logged in
    except CustomUser.DoesNotExist:
        current_user = None
    
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
def removeCart(request, itemid):
    try:
        item = ItemInstance.objects.get(id=itemid)
        current_user = CustomUser.objects.get(username=request.user)
        cart = Cart.objects.get(owner=request.user)
        #set item status
        item.status = 'a'
        item.save(update_fields=["status"])
        #remove the item from the cart by 
        cart.iteminstance_set.remove(item)
        cart.save()
        #To-do: set the item status to 'a', available

    except ItemInstance.DoesNotExist:
        raise Http404("Item does not exist")
    except Cart.DoesNotExist:
        cart = None
    except CustomUser.DoesNotExist:
        current_user = None
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