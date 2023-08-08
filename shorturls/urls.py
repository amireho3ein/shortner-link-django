from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import URLViewSet, URLListView

router = DefaultRouter()
router.register(r'urls', URLViewSet)

urlpatterns = [
    path('urls/list', URLListView.as_view(), name='url-list'),
    path('urls/', include(router.urls)),
    path('urls/<int:pk>/', URLViewSet.as_view({'get': 'retrieve'}), name='url-detail'), 
]