from register.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions
from .models import Invoice
from .serializers import InvoiceSerializer


class InvoiceListAPIView(APIView):
   # permission_classes = [permissions.IsAuthenticated]  # Restrict access to authenticated users
    # permission_classes = [IsAdminUser]  # Restrict access to authenticated users

    def get(self, request):
        orders = Invoice.objects.all()
        serializer = InvoiceSerializer(orders, many=True)
        return Response(serializer.data)

class InvoiceCreateAPIView(APIView):
    #permission_classes = [permissions.IsAdminUser]  # Only admins can create Riders
    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceRetrieveUpdateDeleteView(APIView):
    serrializer_class = InvoiceSerializer

    def get(self, request: Request, invoice_id:int):
        invoice = get_object_or_404(Invoice, pk=invoice_id)

        serializer = self.serrializer_class(instance=invoice)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, invoice_id:int):
        invoice = get_object_or_404(Invoice, pk=invoice_id)
        data = request.data

        serializer = self.serrializer_class(instance=invoice, data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "Invoice Updated Successfully", "data":serializer.data}
            return Response(data= response, status=status.HTTP_202_ACCEPTED)
        
        return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, invoice_id:int):
        invoice = get_object_or_404(Invoice, pk=invoice_id)
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)