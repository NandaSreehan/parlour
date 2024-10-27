from django.db import models

class menu(models.Model): 
    brand=models.CharField(max_length=20)
    flavor=models.CharField(max_length=20)
    price=models.IntegerField()
    quantity=models.IntegerField() 
    


