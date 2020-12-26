from django.db import models

class Item(models.Model):
    name=models.CharField(max_length=50)
    quantity=models.CharField(max_length=20,default='')
    status=models.CharField(max_length=20)
    date=models.DateField()
    id=models.AutoField(primary_key=True);
    def is_valid(self):
        return True

