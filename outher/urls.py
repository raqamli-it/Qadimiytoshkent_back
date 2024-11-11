from django.urls import path

from .dawload import FileDownload
from .views import about_list, kutubxona_detail, muzeylar_detail, muzeylar_list
from .views import OlimlarListAPIView, KutubxonaListAPIView

urlpatterns = [
    path('about/', about_list),
    path('olimlar/', OlimlarListAPIView.as_view(), name='scientist-list'),
    path('kutubxona/', KutubxonaListAPIView.as_view(), name='electronics-list'),
    path('kutubxona/<int:pk>/', kutubxona_detail),
    path('kutubxona/down/<int:pk>/', FileDownload.as_view(), name='file_download'),
    path('muzeylar/', muzeylar_list, name='muzeylar-list'),
    path('muzeylar/<int:pk>/', muzeylar_detail, name='muzeylar-detail'),
]






