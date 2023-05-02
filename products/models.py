from django.db import models

# Here we created our models for the My SQL database. 

class Product(models.Model):
#The First field name is pname = productname
    pname = models.CharField(max_length=200)
#The second Field name is p_description = Product description
    p_description = models.TextField()
#The third field name is price = Price 
    price = models.DecimalField(max_digits=10, decimal_places=2)

