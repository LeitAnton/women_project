from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from women.views import WomenAPIList, WomenAPIUpdate, WomenAPIDestroy
# from ..women.views import WomenAPIList, WomenAPIUpdate, WomenAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

# from women.views import WomenViewSet


# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet, basename='women')


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls))
#     # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
#     # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
# ]


