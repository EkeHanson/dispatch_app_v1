from register.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions
from .models import Rider
from .serializers import (
    RiderCreateSerializer,
    # ManagerSerializer,
)

class RiderListAPIView(APIView):
   # permission_classes = [permissions.IsAuthenticated]  # Restrict access to authenticated users
    # permission_classes = [IsAdminUser]  # Restrict access to authenticated users

    def get(self, request):
        riders = Rider.objects.all()
        # print(riders)
        serializer = RiderCreateSerializer(riders, many=True)
        # print(serializer.data[0])
        return Response(serializer.data)

class RiderCreateAPIView(APIView):
    #permission_classes = [permissions.IsAdminUser]  # Only admins can create Riders

    def post(self, request):
        serializer = RiderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print(request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RiderRetrieveUpdateDeleteView(APIView):
    serrializer_class = RiderCreateSerializer

    def get(self, request: Request, rider_id:int):
        post = get_object_or_404(Rider, pk=rider_id)

        serializer = self.serrializer_class(instance=post)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, rider_id:int):
        post = get_object_or_404(Rider, pk=rider_id)
        data = request.data

        serializer = self.serrializer_class(instance=post, data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "Rider Updated Successfully", "data":serializer.data}
            return Response(data= response, status=status.HTTP_202_ACCEPTED)
        
        return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, rider_id:int):
        post = get_object_or_404(Rider, pk=rider_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
