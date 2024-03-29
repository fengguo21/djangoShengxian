# goods/filters.py

import django_filters

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    '''
    商品过滤的类
    '''
    #两个参数，name是要过滤的字段，lookup是执行的行为，‘小与等于本店价格’
    price_min = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    ordering_fields = ('id',)

    class Meta:
        model = Goods

        fields = {
            'goods_brief': ['contains'],
            'name': ['exact']
        }
