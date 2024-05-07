from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

def validateAmount(quantity,price,amount):
    if amount != (quantity*price):
        raise ValidationError(
            _("%(amount)s is not a valid amount"),
            params={"amount": amount},
        )
        
        
def totalAmount(itemAmount,sundryAmount,totalAmount):
    if totalAmount != itemAmount+ sundryAmount:
        raise ValidationError(
            _("%(totalAmount)s is not a valid amount"),
            params={"totalamount": totalAmount},
        )
        
        
def great_than_zero(value):
    if value <= 0:
        raise ValidationError(
            _("%(value)s is not a valid number"),
        )
        
        
    
        

class InvoiceHeader(models.Model):
    Date : models.DateTimeField(default=timezone.now(), editable= False)
    InvoiceNumber : models.IntegerField(unique=True)
    CustomerName: models.CharField
    BillingAddress: models.CharField
    ShippingAddress : models.CharField
    GSTIN: models.CharField
    TotalAmount: models.DecimalField(validators=[totalAmount(InvoiceItems.Amount,InvoiceBillSundry().Amount,self.TotalAmount)])
    
    
    

class InvoiceItems(models.Model):
    itemName : models.CharField
    Quantity : models.DecimalField(validators=[great_than_zero])
    Price : models.DecimalField(validators=[great_than_zero])
    Amount: models.DecimalField(validators=[validateAmount(self.Quantity,self.Price,self.Amount)])
    
    
    
    
class InvoiceBillSundry(models.Model):
    billSundryName :models.CharField
    Amount : models.CharField
    
    
    
