from django.db import models

class Track (models.Model):
    tname =models.CharField(max_length=50)
    def __str__(self):
        return self.tname
class Std (models.Model):
    fname = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=50, null=True)
    age =models.IntegerField()
    std_track= models.ForeignKey(Track ,on_delete=models.CASCADE)
    def __str__(self):
        return self.fname+' '+self.lname
    
    def is_graduated(self):
        if (self.age >= 10):
            return True
        else:
            return False
    
    is_graduated.boolean = True 
    is_graduated.short_description = 'post graduate'