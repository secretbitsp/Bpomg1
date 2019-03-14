from django.db import models
from phone_field import PhoneField

class Contact(models.Model):
     vezeteknev = models.CharField(max_length=50)
     keresztnev = models.CharField(max_length=50)
     email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
     phone = PhoneField(blank=True, help_text='Amin eltudjuk érni')
     gepkocsimarkaja = models.CharField(max_length=50, help_text='Példa: Opel')
     gepkocsitipus = models.CharField(max_length=50, help_text='Példa: Astra')
     gepkocsirendszama = models.CharField(max_length=7, help_text='Példa: AAA - 111')
     uzenet = models.TextField()



     def __str__(self):
         return f'{self.vezeteknev} {self.keresztnev}'
