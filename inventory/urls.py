from django.urls import path
from .views import (
    inventory_list,
    create_product,
    update_product,
    detail_product,
    delete_product,
)

app_name = 'inventory'

urlpatterns = [
    path('',inventory_list.as_view(), name="list-view" ),
    path('create/',create_product.as_view(), name='create'),
    path('<int:pk>/',detail_product.as_view(), name='detail' ),
    path('<int:pk>/update/', update_product.as_view(), name='update'),
    path('<int:pk>/delete/', delete_product.as_view(), name='delete')


]