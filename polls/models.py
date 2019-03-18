from django.db import models
from phone_field import PhoneField

class Contact(models.Model):
     Vezetéknév = models.CharField(max_length=50)
     Keresztnév = models.CharField(max_length=50)
     Email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
     Telefonszám = PhoneField(blank=True, help_text='Amin eltudjuk érni')
     Gépkocsimárkája = models.CharField(max_length=50, help_text='Példa: Opel')
     Gépkocsitipusa = models.CharField(max_length=50, help_text='Példa: Astra')
     Gépkocsirendszáma = models.CharField(max_length=7, help_text='Példa: AAA - 111')
     Üzenet = models.TextField()



     def __str__(self):
         return f'{self.vezeteknev} {self.keresztnev}'
