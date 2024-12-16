from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to="products/")
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)
    # slug = models.CharField(max_length=50)
    # objects = models.Manager()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


