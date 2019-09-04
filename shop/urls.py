from django.urls import	path
from . import views
app_name = 'shop'
urlpatterns	= [
    path('', views.product_list, name='product_list'),
	path('api/', views.cat_list, name='cat_list'),
    path('api/login/', views.login, name='login'),
    path('api/create/', views.create_cat, name='create'),

    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
	path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]