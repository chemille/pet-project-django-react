from django.http import JsonResponse
from .models import Pet
from .serializers import PetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Remember CRUD: create, read, update, delete
# Also remember http request methods: get, post, put, delete

# @ decorators
@api_view(['GET', 'POST'])
def pet_list(request):

    if request.method == 'GET':
        # get all the pets
        pets = Pet.objects.all()
        # serialize them
        serializer = PetSerializer(pets, many=True)
        # return json
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        # add a pet by taking the data they sent us, deserialize it, and create a pet object out of it
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # Response comes from the django REST framework and it is the preferred way of doing things

@api_view(['GET', 'PUT', 'DELETE'])        
def pet_detail(request, id):

    try:
        pet = Pet.objects.get(pk=id)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PetSerializer(pet)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


################################################
# from django.shortcuts import render
# from rest_framework.views import APIView
# from .models import *
# from .serializers import *
# from rest_framework.response import Response

# class ReactView(APIView):
#     def get(self, request):
#         output = [{"name": output.name,
#                    "description": output.description}
#                    for output in Pet.objects.all()]
#         return Response(output)
    
#     def post(self, request):
#         serializer = PetSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)