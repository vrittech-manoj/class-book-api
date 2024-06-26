from rest_framework import viewsets
from .models import Books
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


#******serializers class*************

from rest_framework import serializers

class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

#***********************************


class BooksViewsets(viewsets.ModelViewSet):
    queryset  = Books.objects.all()
    serializer_class = BooksSerializers
    # permission_classes = [IsAuthenticated]

    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]

    search_fields = ['id']
    # ordering_fields = ['id','name']
    filterset_fields = {
    #    'quantity': ['exact','gte','lte'],
        # 'price': ['exact', 'gte', 'lte'],
    }

    
   