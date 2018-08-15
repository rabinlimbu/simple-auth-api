from rest_framework import mixins, permissions, viewsets
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from .models import Address
from .serializers import AddressSerializer


class AddressViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class AddressListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    # Specifying model = Foo is effectively the same as specifying queryset = Foo.objects.all(), where
    # objects stands for Foo’s default manager
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
    '''
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    '''
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)