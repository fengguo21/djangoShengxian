"""renyakun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
import xadmin
from django.views.static import serve
from renyakun.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
# from goods.views import GoodsListView
from rest_framework.routers import DefaultRouter
from goods.views import GoodsListViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#配置goods的url
router.register('goods', GoodsListViewSet)




urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    path('', include(router.urls)),
    # path('goods/',GoodsListViewSet, name='goods-list'),
    path('docs',include_docs_urls(title='仙剑奇侠传')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
