from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SuperType
from .serializers import SuperTypeSerializer
from rest_framework import status

# from supers import serializers 

# Create your views here.

@api_view(['GET', 'POST'])
def super_type_list(request):
    if request.method == 'GET':
        super_type = SuperType.objects.all()
        serializer = SuperTypeSerializer(super_type, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_type_detail(request,pk):
    super_type = get_object_or_404(SuperType, pk=pk)
    if request.method =="GET":
        serializer = SuperTypeSerializer(super_type)
        return Response(serializer.data)
    elif request.method =="PUT":
        serializer = SuperTypeSerializer(super_type)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super_type.delete()
        return Response(satus=status.HTTP_204_NO_CONTENT)