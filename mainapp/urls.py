from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView

app_name='mainapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),

    path('shop', views.product_list, name='shop'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search', views.search_results, name='search_results'),
    path('compare', views.compare_products, name='compare-products'),
    path('allproducts/<int:id>', views.allproducts, name='allproducts'),

    path('product-create', views.product_create, name='product-create'),
    path('product-edit/<int:id>/', views.product_edit, name='product-edit'),
    path('product-delete/<int:id>/', views.product_delete, name='product-delete'),

    path('cart', views.cart_view, name='cart'),
    path('checkout', views.checkout_view, name='checkout'),
    path('contact', views.contact_view, name='contact'),
    path('terms', views.terms_view, name='terms'),

    path('your-account', views.youraccount_view, name='your-account'),
    path('first-account-update', views.profilefirstupdateview, name='first-account-update'),
    path('orderhistory', views.order_history, name='order-history'),
    path('return-order/<int:id>', views.return_order, name='return-order')
]