from django.db.models import Q
from django_filters import filters, CharFilter
from django_filters import FilterSet
from django_filters.constants import EMPTY_VALUES


class SearchFilterField(CharFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        if self.distinct:
            qs = qs.distinct()
        lookups = (
            '%s__%s' % (self.field_name, lookup_expr)
            for lookup_expr in ('contains', 'icontains')
        )
        qs_lookup_expression = Q()
        for lookup in lookups:
            qs_lookup_expression |= Q(**{lookup: value})
        qs = self.get_method(qs)(qs_lookup_expression)
        return qs


class CarFilter(FilterSet):
    price_max = filters.NumberFilter(field_name='price', lookup_expr='lte')
    price_min = filters.NumberFilter(field_name='price', lookup_expr='gte')
    mark = SearchFilterField(field_name='mark')
    model = SearchFilterField(field_name='model')
    year_max = filters.NumberFilter(field_name='year_manufactured', lookup_expr='lte')
    year_min = filters.NumberFilter(field_name='year_manufactured', lookup_expr='gte')
    mileage_max = filters.NumberFilter(field_name='mileage', lookup_expr='lte')
    mileage_min = filters.NumberFilter(field_name='mileage', lookup_expr='gte')
