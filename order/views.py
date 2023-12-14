from register.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions
from .models import Order
from .serializers import OrderSerializer
from rest_framework import generics

class OrderListByEstablishmentAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        establishment_id = self.kwargs['establishment_id']
        return Order.objects.filter(establishment_id=establishment_id)

class OrderListAPIView(APIView):
   # permission_classes = [permissions.IsAuthenticated]  # Restrict access to authenticated users
    # permission_classes = [IsAdminUser]  # Restrict access to authenticated users

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class OrderCreateAPIView(APIView):
    #permission_classes = [permissions.IsAdminUser]  # Only admins can create Riders
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderRetrieveUpdateDeleteView(APIView):
    serrializer_class = OrderSerializer

    def get(self, request: Request, order_id:int):
        order = get_object_or_404(Order, pk=order_id)

        serializer = self.serrializer_class(instance=order)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, order_id:int):
        order = get_object_or_404(Order, pk=order_id)
        data = request.data

        serializer = self.serrializer_class(instance=order, data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "Order Updated Successfully", "data":serializer.data}
            return Response(data= response, status=status.HTTP_202_ACCEPTED)
        
        return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, order_id:int):
        order = get_object_or_404(Order, pk=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)