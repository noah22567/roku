from .models import DevicesModel, DeviceCommands
import django_filters

class DeviceModelFilter(django_filters.FilterSet):
    status_include = django_filters.CharFilter(field_name='device_model', method='filter_status_include')

    def filter_status_include(self, queryset, name, value):
        if not value:
            return queryset
        values = ''.join(value.split(' ')).split(',')
        queryset = queryset.filter(status__in=values)
        return queryset

    class Meta:
        model = DevicesModel
        fields = ['device_brand', 'device_model']


# class DeviceCommandFilter(django_filters.FilterSet):
#     status_include = django_filters.CharFilter(field_name='command', method='filter_status_include')
#
#     def filter_status_include(self, queryset, name, value):
#         if not value:
#             return queryset
#         values = ''.join(value.split(' ')).split(',')
#         queryset = queryset.filter(status__in=values)
#         return queryset
#
#     class Meta:
#         model = DeviceCommands
#         fields = ['command_list','command','endpoint','method','body']



