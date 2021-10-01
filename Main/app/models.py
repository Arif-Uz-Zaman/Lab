from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Message = models.TextField(max_length=100)
    def __str__(self):
        return f"Name :{self.Name}--Email : {self.Email} -- Message :{self.Message}"