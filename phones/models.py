from django.db import models
from django.utils.text import slugify



class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to="products/")
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50, unique=True)
    # objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

    # def __repr__(self):
    #     return f"<Phone {self.name}>"
    # или можно вообще убрать __repr__, для Django он не обязателен


