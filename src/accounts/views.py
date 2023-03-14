from rest_framework import viewsets

from .models import User
from .serializers import AccountsSerializer


class AccountsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountsSerializer
