from django.db import models

# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    locked=models.BooleanField(default=False)
    password=models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['-date_created']