import django_filters
from Acoes.models import Acoes

class AcoesFiltro(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    data_inicio = django_filters.DateFilter('data_inicio')
    data_fim = django_filters.DateFilter('data_fim')
    local = django_filters.CharFilter(lookup_expr='icontains')
    descricao = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Acoes
        fields = {'responsavel', 'tipo'}