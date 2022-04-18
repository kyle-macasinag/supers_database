from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Supers
from .serializers import SupersSerializer
from rest_framework import status

# from supers import serializers 

# Create your views here.

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = Supers.objects.all()
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request,pk):
    supers = get_object_or_404(Supers, pk=pk)
    if request.method =="GET":
        serializer = SupersSerializer(supers)
        return Response(serializer.data)
    elif request.method =="PUT":
        serializer = SupersSerializer(supers)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(satus=status.HTTP_204_NO_CONTENT)