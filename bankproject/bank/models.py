from django.db import models

# Create your models here.
class pdet(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField()
    dob=models.DateField()
    address=models.TextField(default="not given")
    mob=models.IntegerField()
    mail=models.EmailField()

class District(models.Model):
    name= models.CharField(max_length=250,blank=True,null=True)
    def __str__(self):
        return str(self.name)

class Branch(models.Model):
    name=models.CharField(max_length=250,blank=True,null=True)
    district=models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.district}-{self.name}"

