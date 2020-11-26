from django.urls import path
from . import views
from .views import SignUpView
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('items/', views.ItemListView.as_view(), name='items'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
	path('products/', views.ProductListView.as_view(), name='products'),
	path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
	path('iteminstance/<str:pk>', views.ItemInstanceDetailView.as_view(), name='iteminstance-detail'),
	path('signup/', SignUpView.as_view(), name='signup'),
	path('cart/<int:pk>', views.CartView.as_view(), name='cart'),
	path('cart/<str:itemid>', views.addToCart, name='addToCart'),
]