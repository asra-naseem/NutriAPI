from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Smoothie,Ingredient,SmoothieIngredient
from .serializers import SmoothieSerializer,IngredientSerializer,SmoothieIngredientSerializer

class SmoothieList(APIView):
    """
    List all smoothies, or create a new smoothie.
    """

    def get(self, request, format=None):
        smoothies = Smoothie.objects.all()
        serializer = SmoothieSerializer(smoothies, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SmoothieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class IngredientList(APIView):
    """
    List all smoothies, or create a new smoothie.
    """

    def get(self, request, format=None):
        ingredient = Ingredient.objects.all()
        serializer1 = IngredientSerializer(ingredient,many=True)
        return Response(serializer1.data)
    
    def post(self, request, format=None):
        serializer1 = IngredientSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data, status=status.HTTP_201_CREATED)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST) 

class SmoothieDetail(APIView):
    """
    Retrieve a single smoothie by its ID.
    """

    def get_object(self, pk):
        try:
            return Smoothie.objects.get(pk=pk)
        except Smoothie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        smoothie = self.get_object(pk)
        serializer = SmoothieSerializer(smoothie)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        smoothie = self.get_object(pk)
        serializer = SmoothieSerializer(smoothie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        smoothie = self.get_object(pk)
        smoothie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class SmoothieIngredientList(APIView):
    """
    List all smoothies, or create a new smoothie.
    """

    def get(self, request, format=None):
        Singredient = SmoothieIngredient.objects.all()
        serializer = SmoothieIngredientSerializer(Singredient,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SmoothieIngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
