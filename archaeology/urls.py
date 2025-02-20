from django.urls import path

from .views import ( archaeology_list, archaeology_detail,
                    news_list, news_detail, category_list, 
                    category_detail,  items_detail, items_list,
                    archaeology_categories_list, archaeology_item_detail, archaeology_items_list,
                    archaeology_category_items_list, archaeology_category_item_detail,
                    )
# archaeology_type_list, archaeology_type_detail,archaeology_type_category_item_detail,
#                     archaeology_type_category_items_list, archaeology_type_categories_list,
#                     archaeology_type_item_detail, archaeology_type_items_list,

urlpatterns = [
    path('categories/', category_list),
    path('categories/<int:pk>/', category_detail),
    path('items/', items_list),
    path('items/<int:pk>/', items_detail),
    path('news/', news_list),
    path('news/<int:pk>/', news_detail),

    # Items
    path('items/', items_list, name='items-list'),
    path('items/<int:pk>/', items_detail, name='item-detail'),  # Bitta itemni olish    


    # Archaeology list >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>...
    path('archaeologies/', archaeology_list),

    # Archaeology detail
    path('archaeologies/<int:archaeology_id>/', archaeology_detail),

    # Archaeology bo'yicha items ro'yxati
    path('archaeologies/<int:archaeology_id>/items/', archaeology_items_list),

    # Archaeology va item detail
    path('archaeologies/<int:archaeology_id>/items/<int:item_id>/', archaeology_item_detail),

    # Archaeology bo'yicha kategoriyalar ro'yxati
    path('archaeologies/<int:archaeology_id>/categories/', archaeology_categories_list),

    # Archaeology va kategoriya bo'yicha items ro'yxati
    path('archaeologies/<int:archaeology_id>/categories/<int:category_id>/items/',
         archaeology_category_items_list),

    # Archaeology, kategoriya va item detail
    path('archaeologies/<int:archaeology_id>/categories/<int:category_id>/items/<int:item_id>/',
         archaeology_category_item_detail),

]


