from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

from .models import Property
from .serializers import CustomTokenObtainPairSerializer, PropertySerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class PropertyList(APIView):
    # authentication_classes = [SessionAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.data:
            return Response({'error': 'GET requests should not include a request body.'}, status=status.HTTP_400_BAD_REQUEST)
        libros = Property.objects.all()
        serializer = PropertySerializer(libros, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class PropertyInsert(APIView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PropertyDetail(APIView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if request.data:
            return Response({'error': 'GET requests should not include a request body.'}, status=status.HTTP_400_BAD_REQUEST)
        property = Property.objects.get(pk=pk)
        serializer = PropertySerializer(property)
        return Response(serializer.data)

    def put(self, request, pk):
        property = Property.objects.get(pk=pk)
        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        libro = Property.objects.get(pk=pk)
        libro.delete()
        return Response({'Item deleted successfully'}, status=200)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer 