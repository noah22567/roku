from rest_framework_api_key.models import APIKey
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, ListAPIView


# will have to extend api key class for specific users or use user auth on client side


# make key
# class GetAPIKey(ListCreateAPIView):
#
#     def get_queryset(self):
#         client_ip = self.request.data['client_ip']


# view key
# class DeleteAPIKey(DestroyAPIView):



