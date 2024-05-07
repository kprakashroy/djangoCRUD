from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes,authentication_classes, permission_classes
import json

from django.contrib.auth.models import User

from base.models import InvoiceBillSundry,InvoiceHeader,InvoiceItems
from .serializer import invoiceHeaderSerializer,invoiceItemsSerializer,invoiceSundrySerializer




def retreive(request):
    id = request.data['id']
    invoiceheader = InvoiceHeader.objects.get(id = id)
    
    if invoiceheader.DoesNotExist:
        return Response({"msg":"According to this id data not belongs"})
    
    
    invoiceBillSundry = InvoiceBillSundry.objects.get(id =id)
    invoiceitems = InvoiceItems.objects.get(id = id)
    response = {**invoiceheader,**invoiceBillSundry,**invoiceitems}
    
    return Response(response)


def create(request):
    data1 = {"InvoiceNumber": request.data['InvoiceNumber'],
    "CustomerName": request.data['CustomerName'],
    "BillingAddress": request.data['BillingAddress'],
    "ShippingAddress": request.data['ShippingAddress'],
    "GSTIN": request.data['GSTIN'],
    "TotalAmount": request.data['TotalAmount']}
    
    headerSerializer = invoiceHeaderSerializer(data = data1 )
    
    if headerSerializer.is_valid():
        data2 = {"itemName": request.data['itemName'],
    "Quantity": request.data['Quantity'],
    "Price": request.data['Price'],
    "Amount": request.data['Amount']}
        invoiceItemSerrial =  invoiceItemsSerializer(data = data2)
        
        if invoiceItemSerrial.is_valid():
            data3 = {"billSundryName": request.data['billSundryName'],
    "Amount": request.data['Amount']}
            
            invoiceSlurrySerial = invoiceSundrySerializer(data = data3)
            
            if invoiceSlurrySerial.is_valid():
                headerSerializer.save()
                invoiceItemSerrial.save()
                invoiceSlurrySerial.save()
                
    returnData = {**headerSerializer.data,**invoiceItemSerrial.data,**invoiceSlurrySerial.data}
    
    return Response(returnData)
            
        
        

    
    
def update(request):
    id = request.data['id']
    data1 = InvoiceHeader.objects.get(pk=id)
    data1 = {"InvoiceNumber": request.data['InvoiceNumber'],
    "CustomerName": request.data['CustomerName'],
    "BillingAddress": request.data['BillingAddress'],
    "ShippingAddress": request.data['ShippingAddress'],
    "GSTIN": request.data['GSTIN'],
    "TotalAmount": request.data['TotalAmount']}
    data1.save()
    data2 = InvoiceItems.objects.get(pk=id)
    data2 = {"itemName": request.data['itemName'],
    "Quantity": request.data['Quantity'],
    "Price": request.data['Price'],
    "Amount": request.data['Amount']}
    data2.save()
    data3 = InvoiceBillSundry.objects.get(pk=id)
    data3 = {"billSundryName": request.data['billSundryName'],
    "Amount": request.data['Amount']}
    data3.save()
    
    
    
    return Response({**data1,**data2,**data3})


def delete(request):
    id = request.data['id']
    InvoiceBillSundry.objects.filter(id=id).delete()
    InvoiceHeader.objects.filter(id=id).delete()
    InvoiceItems.objects.filter(id=id).delete()
    return Response("data deleted")


def listAll(request):
    
    items = InvoiceHeader.objects.all()
    return Response(items)




    
    


