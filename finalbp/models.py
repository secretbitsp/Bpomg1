from django.db import models




class Brand(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)

    def brand_name(self):
        return self.brand.company_name

    def __str__(self):
        return self.name


class Fleet(models.Model):
    car = models.ForeignKey(Car, on_delete = models.CASCADE)
    description = models.CharField(max_length=100)

    def car_name(self):
        return self.car.name

    def brand(self):
        return self.car.brand.company_name

    def __str__(self):
        return self.description



class Hahuautok(models.Model):
    kep = models.ImageField(blank=True, null=True)



class Hahudeta(models.Model):
        rank = models.CharField(max_length=100)
        marka = models.CharField(max_length=100)
        kategoria = models.CharField(max_length=100)
        modell = models.CharField(max_length=100)
        tipus = models.CharField(max_length=100)


        def __str__(self):
            return self.rank
