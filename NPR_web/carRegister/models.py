from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Point(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    x_relative = models.FloatField(default=0.0)
    camera = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.x}, {self.y}, {self.camera}"


class WhiteList(models.Model):
    car_number = models.CharField('Номер автомобиля', max_length=11)
    car_mark = models.CharField("Марка автомобиля", max_length=50)
    car_model = models.CharField("Модель автомобиля", max_length=50)
    car_year = models.IntegerField("Год выпуска автомобиля",
                                   validators=[
                                       MaxValueValidator(2023),
                                       MinValueValidator(1930)
                                   ]
                                   )

    def __str__(self):
        return f"{self.car_number}, {self.car_mark}"


class CarRegister(models.Model):
    employee = models.ForeignKey(WhiteList, on_delete=models.CASCADE)
    type_of_action = models.CharField("Название действия", max_length=20)
    date = models.DateTimeField("Время")
    image = models.ImageField(upload_to='carRegister/')

    def __str__(self):
        return f"{self.employee.car_number}, {self.date}"


