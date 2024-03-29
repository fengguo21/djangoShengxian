from goods.serializers import GoodsSerializer
from .models import Goods
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .filters import GoodsFilter
from django_filters.rest_framework import DjangoFilterBackend

class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 10
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100

from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics


class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    '商品列表页'

    # 分页
    pagination_class = GoodsPagination
    #这里必须要定义一个默认的排序,否则会报错
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer

    # 设置filter的类为我们自定义的类
    filter_class = GoodsFilter



