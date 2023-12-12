from register.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions
from register.permissions import IsAdminUser
from .models import Establishment
from .serializers import (
    EstablishmentSerializer,
    # ManagerSerializer,
)

class EstablishmentListAPIView(APIView):
   # permission_classes = [permissions.IsAuthenticated]  # Restrict access to authenticated users
    # permission_classes = [IsAdminUser]  # Restrict access to authenticated users

    def get(self, request):
        establishments = Establishment.objects.all()
        # print(establishments)
        serializer = EstablishmentSerializer(establishments, many=True)
        return Response(serializer.data)

class EstablishmentCreateAPIView(APIView):
    #permission_classes = [permissions.IsAdminUser]  # Only admins can create Riders

    def post(self, request):
        serializer = EstablishmentSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstablishmentRetrieveUpdateDeleteView(APIView):
    serrializer_class = EstablishmentSerializer

    def get(self, request: Request, establishment_id:int):
        establishment = get_object_or_404(Establishment, pk=establishment_id)

        serializer = self.serrializer_class(instance=establishment)
        print(establishment_id)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, establishment_id:int):
            establishment = get_object_or_404(Establishment, pk=establishment_id)
            data = request.data

            serializer = self.serrializer_class(instance=establishment, data=data)

            if serializer.is_valid():
                serializer.save()

                response = {"message": "Establishment Updated Successfully", "data":serializer.data}
                return Response(data= response, status=status.HTTP_202_ACCEPTED)
            
            return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, establishment_id:int):
        establishment = get_object_or_404(Establishment, pk=establishment_id)
        establishment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
