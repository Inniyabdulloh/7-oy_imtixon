from django.db import models

# Create your models here.


class Xodimlar(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.full_name


class Davomat(models.Model):
    xodim = models.ForeignKey(Xodimlar, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.xodim} - {self.date}"