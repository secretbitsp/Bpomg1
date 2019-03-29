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


class CachedImage(models.Model):
    url = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='HahuImg', blank=True, null=True)
    car = models.ForeignKey(Hahudeta, on_delete = models.CASCADE, related_name='images')

    def cache(self):
        """Store image locally if we have a URL"""

        if self.url and not self.photo:
            result = urllib.urlretrieve(self.url)
            self.photo.save(
                    os.path.basename(self.url),
                    File(open(result[0], 'rb'))
                    )
            self.save()
