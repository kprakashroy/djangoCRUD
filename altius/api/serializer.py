from rest_framework import serializers
from base.models import InvoiceBillSundry,InvoiceHeader,InvoiceItems

class invoiceHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceHeader
        fields = '__all__'
        
        
        


class invoiceSundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceBillSundry
        fields = '__all__'
        
        
        
class invoiceItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItems
        fields = '__all__'