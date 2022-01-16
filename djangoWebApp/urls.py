from django.contrib import admin
from django.urls import path
from home.views import home_view
from products.views import product_list, product_add, product_remove
from history.views import history_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('productList/', product_list),
    path('productList/Add/', product_add),
    path('remove', product_remove),
    path('history/', history_list),

]
