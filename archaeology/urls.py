from django.urls import path

from .views import (archaeology_list, archaeology_detail,
                    news_list, news_detail, category_list, archaeology_type_list, archaeology_type_detail,
                    category_detail, archaeology_type_category_item_detail,
                    archaeology_type_category_items_list, archaeology_type_categories_list,
                    archaeology_type_item_detail, archaeology_type_items_list, items_detail, items_list,
                    archaeology_categories_list, archaeology_item_detail, archaeology_items_list,
                    archaeology_category_items_list, archaeology_category_item_detail,
                    )

urlpatterns = [
    path('categories/', category_list),
    path('categories/<int:pk>/', category_detail),
    path('items/', items_list),
    path('items/<int:pk>/', items_detail),
    path('news/', news_list),
    path('news/<int:pk>/', news_detail),
    path('archaeology-types/', archaeology_type_list),
    path('archaeology-types/<int:pk>/', archaeology_type_detail),

    path('archaeologies_type/', archaeology_type_list),
    path('archaeologies_type/<int:archaeology_id>/', archaeology_type_detail),

    # ArchaeologyType bo'yicha items ro'yxati
    path('archaeologies_type/<int:archaeology_id>/items/', archaeology_type_items_list),

    # ArchaeologyType bo'yicha item detail
    path('archaeologies_type/<int:archaeology_id>/items/<int:item_id>/', archaeology_type_item_detail),

    # ArchaeologyType bo'yicha kategoriyalar
    path('archaeologies_type/<int:archaeology_id>/categories/', archaeology_type_categories_list),

    # ArchaeologyType va kategoriya bo'yicha items ro'yxati
    path('archaeologies_type/<int:archaeology_id>/categories/<int:category_id>/items/', archaeology_type_category_items_list),

    # ArchaeologyType, kategoriya va item detail
    path('archaeologiestype/<int:archaeology_id>/categories/<int:category_id>/items/<int:item_id>/', archaeology_type_category_item_detail),


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


