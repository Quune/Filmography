from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view

from Backend.models import Movie


@api_view(['GET', 'POST', 'DELETE'])
def file_list(request):
    try:
        movie = Movie.objects.all()
    except Movie.DoesNotExist:
        return JsonResponse({'message': 'The File does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def file_detail(request, pk):
    # find File by pk (id) with type of file (M,E)
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return JsonResponse({'message': 'The File does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # GET / PUT / DELETE File
