from rest_framework import viewsets
from .models import Books


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