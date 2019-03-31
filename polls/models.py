from django.db import models
from phone_field import PhoneField

class Contact(models.Model):
     Vezetéknév = models.CharField(max_length=50)
     Email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
     Telefonszám = PhoneField(blank=True, help_text='Amin eltudjuk érni')

     Üzenet = models.TextField()



     def __str__(self):
         return f'{self.vezeteknev} {self.keresztnev}'
