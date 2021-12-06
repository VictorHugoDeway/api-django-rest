from rest_framework import viewsets
from list.models import List
from list.serializer import ListSerializer

class ListsViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer