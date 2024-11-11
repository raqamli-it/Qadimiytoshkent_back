from rest_framework import filters
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from outher.models import About, Muzeylar, Kutubxona, Olimlar
from outher.serializer import AboutSerializer, MuzeylarSerializer, KutubxonaSerializer, OlimlarSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def about_list(request):
    abouts = About.objects.all()
    serializer = AboutSerializer(abouts, many=True)
    return Response(serializer.data)


class OlimlarListAPIView(ListAPIView):
    queryset = Olimlar.objects.all().order_by("id")
    serializer_class = OlimlarSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['fullname']


class KutubxonaListAPIView(ListAPIView):
    queryset = Kutubxona.objects.all().order_by("id")
    serializer_class = KutubxonaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = [AllowAny]


@api_view(['GET'])
@permission_classes([AllowAny])
def kutubxona_detail(request, pk):
    try:
        kitob = Kutubxona.objects.get(pk=pk)
    except Kutubxona.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = KutubxonaSerializer(kitob)
    serializer_data = serializer.data

    if serializer_data.get('image'):
        serializer_data['image'] = request.build_absolute_uri(serializer_data['image'])
    if serializer_data.get('file'):
        serializer_data['file'] = request.build_absolute_uri(serializer_data['file'])

    return Response(serializer_data)

@api_view(['GET'])
@permission_classes([AllowAny])
def muzeylar_list(request):
    muzeylar = Muzeylar.objects.all().order_by("id")
    serializer = MuzeylarSerializer(muzeylar, many=True)
    serializer_data = serializer.data

    for obj in serializer_data:
        if obj.get('image'):
            obj['image'] = request.build_absolute_uri(obj['image'])
        if obj.get('video'):
            obj['video'] = request.build_absolute_uri(obj['video'])

    return Response(serializer_data)


@api_view(['GET'])
@permission_classes([AllowAny])
def muzeylar_detail(request, pk):
    try:
        muzey = Muzeylar.objects.get(pk=pk)
    except Muzeylar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MuzeylarSerializer(muzey)
    serializer_data = serializer.data

    if serializer_data.get('image'):
        serializer_data['image'] = request.build_absolute_uri(serializer_data['image'])
    if serializer_data.get('video'):
        serializer_data['video'] = request.build_absolute_uri(serializer_data['video'])

    return Response(serializer_data)
