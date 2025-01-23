from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import status

from .models import Archaeology, Items, News, Category, ArchaeologyType
from .pagination import ResultsSetPagination
from .serializers import NewsSerializers, CategorySerializer, ArchaeologySerializers, \
    ArchaeologyTypeForItemSerializers, ItemsSerializers, ArchaeologyListSerializers


@api_view(['GET'])
@permission_classes([AllowAny])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)  # Kategoriyani ID orqali olish
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category, context={'request': request})  # Serializerdan foydalanish
    return Response(serializer.data)  # Natijani qaytarish


@api_view(['GET'])
@permission_classes([AllowAny])
def items_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 20
    comments = Items.objects.all().order_by("id")
    result_page = paginator.paginate_queryset(comments, request)
    serializer = ItemsSerializers(result_page, many=True, context={'request': request})

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def items_detail(request, pk):
    try:
        items = Items.objects.get(pk=pk)
    except Items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    items.view_count += 1
    items.save()

    serializer = ItemsSerializers(items, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def news_list(request):
    comments = News.objects.all().order_by("id")
    serializer = NewsSerializers(comments, many=True)
    serializer_url = serializer.data
    for obj_url in serializer_url:
        # Process image field for News model
        if obj_url.get('image'):
            obj_url['image'] = request.build_absolute_uri(obj_url['image'])
        # Process image fields for NewsPicture model
        for obj in obj_url['news_picture']:
            if obj.get('image'):
                obj['image'] = request.build_absolute_uri(obj['image'])
    return Response(serializer_url)


@api_view(['GET'])
@permission_classes([AllowAny])
def news_detail(request, pk):
    try:
        about = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NewsSerializers(about)
    serializer_data = serializer.data

    # Process image field for News model
    if serializer_data.get('image'):
        serializer_data['image'] = request.build_absolute_uri(serializer_data['image'])

    # Process image fields for NewsPicture model
    if 'news_picture' in serializer_data:
        for obj in serializer_data['news_picture']:
            if obj.get('image'):
                obj['image'] = request.build_absolute_uri(obj['image'])

    return Response(serializer_data)  # 111


@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_type_list(request):
    archaeology_types = ArchaeologyType.objects.all()
    serializer = ArchaeologyTypeForItemSerializers(archaeology_types, many=True)
    serializer_url = serializer.data
    for obj_url in serializer_url:
        # Process image field for News model
        if obj_url.get('image'):
            obj_url['image'] = request.build_absolute_uri(obj_url['image'])

    return Response(serializer_url)


# ArchaeologyType detail
@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_type_detail(request, archaeology_id):
    archaeology_type = get_object_or_404(ArchaeologyType, id=archaeology_id)
    serializer = ArchaeologyTypeForItemSerializers(archaeology_type, context={'request': request})
    serializer_data = serializer.data
    if serializer_data.get('image'):
        serializer_data['image'] = request.build_absolute_uri(serializer_data['image'])

    return Response(serializer_data)


# ArchaeologyType bo'yicha items ro'yxati
@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_type_items_list(request, archaeology_id):
    archaeology = get_object_or_404(ArchaeologyType, id=archaeology_id)
    items = archaeology.items_type.all()
    serializer = ItemsSerializers(items, many=True, context={'request': request})

    serialized_data = serializer.data
    for obj in serialized_data:
        if obj.get('image'):
            obj['image'] = request.build_absolute_uri(obj['image'])

    return Response(serialized_data)


# ArchaeologyType va item detail
@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_type_item_detail(request, archaeology_id, item_id):
    item = get_object_or_404(Items, archaeology_type_id=archaeology_id, id=item_id)
    serializer = ItemsSerializers(item, context={'request': request})
    serializer_data = serializer.data

    # Convert the image field to an absolute URL if it exists
    if serializer_data.get('image'):
        serializer_data['image'] = request.build_absolute_uri(serializer_data['image'])

    return Response(serializer_data)


# ArchaeologyType bo'yicha kategoriyalar ro'yxati
@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_type_categories_list(request, archaeology_id):
    categories = Category.objects.filter(items__archaeology_type_id=archaeology_id).distinct()
    serializer = CategorySerializer(categories, many=True, context={'request': request})
    serialized_data = serializer.data
    for obj in serialized_data:
        if obj.get('image'):
            obj['image'] = request.build_absolute_uri(obj['image'])

    return Response(serialized_data)


# ArchaeologyType va kategoriya bo'yicha items ro'yxati
@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_type_category_items_list(request, archaeology_id, category_id):
    items = Items.objects.filter(archaeology_type_id=archaeology_id, category_id=category_id)
    serializer = ItemsSerializers(items, many=True, context={'request': request})
    serializer_data = serializer.data

    # Har bir element bo'yicha image URL ni to'liq qaytarish
    for item in serializer_data:
        if item.get('image'):
            item['image'] = request.build_absolute_uri(item['image'])

    return Response(serializer_data)


# ArchaeologyType, kategoriya va item detail
@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_type_category_item_detail(request, archaeology_id, category_id, item_id):
    item = get_object_or_404(Items, archaeology_type_id=archaeology_id, category_id=category_id, id=item_id)
    serializer = ItemsSerializers(item, context={'request': request})
    serializer_data = serializer.data
    if serializer_data.get('image'):
        serializer_data['image'] = request.build_absolute_uri(serializer_data['image'])
    return Response(serializer_data)


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def archaeology_list(request):
#     paginator = PageNumberPagination()
#     paginator.page_size = 30
#     comments = Archaeology.objects.all().order_by("id")
#     result_page = paginator.paginate_queryset(comments, request)
#     serializer = ArchaeologySerializers(result_page, many=True, context={'request': request})
#     serializer_url = serializer.data
#     for obj_url in serializer_url:
#         if obj_url.get('image'):
#             obj_url['image'] = request.build_absolute_uri(obj_url['image'])
#     return Response(serializer_url)


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def archaeology_detail(request, pk):
#     try:
#         archaeology = Archaeology.objects.get(pk=pk)
#     except Archaeology.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     archaeology.view_count += 1
#     archaeology.save()
#
#     serializer = ArchaeologySerializers(archaeology, context={'request': request})
#     return Response(serializer.data)


# Archaeology list
@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_list(request):
    queryset = Archaeology.objects.all().order_by("id")
    paginator = ResultsSetPagination()
    paginated_queryset = paginator.paginate_queryset(queryset, request)

    serializer = ArchaeologyListSerializers(paginated_queryset, many=True, context={'request': request})
    serializer_data = serializer.data

    # Image URL to absolute
    for obj in serializer_data:
        if obj.get('image'):
            obj['image'] = request.build_absolute_uri(obj['image'])

    return paginator.get_paginated_response(serializer_data)


# Archaeology detail
@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_detail(request, archaeology_id):
    archaeology = get_object_or_404(Archaeology, id=archaeology_id)
    serializer = ArchaeologySerializers(archaeology, context={'request': request})
    serializer_data = serializer.data

    # Image URL to absolute
    if serializer_data.get('image'):
        serializer_data['image'] = request.build_absolute_uri(serializer_data['image'])

    return Response(serializer_data)


# Archaeology bo'yicha items ro'yxati
@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_items_list(request, archaeology_id):
    archaeology = get_object_or_404(Archaeology, id=archaeology_id)
    items = archaeology.items_set.all()
    serializer = ItemsSerializers(items, many=True, context={'request': request})

    serialized_data = serializer.data
    for obj in serialized_data:
        if obj.get('image'):
            obj['image'] = request.build_absolute_uri(obj['image'])

    return Response(serialized_data)


# Archaeology va item detail
@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_item_detail(request, archaeology_id, item_id):
    item = get_object_or_404(Items, archaeology_id=archaeology_id, id=item_id)
    serializer = ItemsSerializers(item, context={'request': request})
    serializer_data = serializer.data

    if serializer_data.get('image'):
        serializer_data['image'] = request.build_absolute_uri(serializer_data['image'])

    return Response(serializer_data)


# Archaeology bo'yicha kategoriyalar ro'yxati
@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_categories_list(request, archaeology_id):
    categories = Category.objects.filter(items__archaeology_id=archaeology_id).distinct()
    serializer = CategorySerializer(categories, many=True, context={'request': request})
    serialized_data = serializer.data
    for obj in serialized_data:
        if obj.get('image'):
            obj['image'] = request.build_absolute_uri(obj['image'])

    return Response(serialized_data)


# Archaeology va kategoriya bo'yicha items ro'yxati
@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_category_items_list(request, archaeology_id, category_id):
    items = Items.objects.filter(archaeology_id=archaeology_id, category_id=category_id)
    serializer = ItemsSerializers(items, many=True, context={'request': request})
    serializer_data = serializer.data

    # Har bir element bo'yicha image URL ni to'liq qaytarish
    for item in serializer_data:
        if item.get('image'):
            item['image'] = request.build_absolute_uri(item['image'])

    return Response(serializer_data)


# Archaeology, kategoriya va item detail
@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_category_item_detail(request, archaeology_id, category_id, item_id):
    item = get_object_or_404(Items, archaeology_id=archaeology_id, category_id=category_id, id=item_id)
    serializer = ItemsSerializers(item, context={'request': request})
    serializer_data = serializer.data

    # Har bir element bo'yicha image URL ni to'liq qaytarish
    if serializer_data.get('image'):
        serializer_data['image'] = request.build_absolute_uri(serializer_data['image'])

    return Response(serializer_data)
