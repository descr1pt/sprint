from django.core.files import File
from django.db import models


class MyUser(models.Model):
    mail = models.CharField(max_length=128, unique=True)
    full_name = models.CharField(max_length=128)
    phone = models.IntegerField(unique=True)


class Coord(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    height = models.IntegerField()


class Level(models.Model):
    level_name = models.CharField(max_length=128, unique=True)


class Pereval(models.Model):
    NEW = 'NW'
    PENDING = 'PN'
    ACCEPTED = 'AC'
    REJECTED = 'RJ'
    STATUS_CHOICES = (
        ('NW', 'New'),
        ('AC', 'Accepted'),
        ('PN', 'Pending'),
        ('RJ', 'Rejected'),
    )
    beautyTitle = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    other_titles = models.CharField(max_length=128)
    connect = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NEW)
    coord_id = models.OneToOneField(Coord, on_delete=models.CASCADE)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    winter_level_id = models.ManyToManyField(Level, through='PerevalLevel')
    spring_level_id = models.ManyToManyField(Level, through='PerevalLevel')
    summer_level_id = models.ManyToManyField(Level, through='PerevalLevel')
    autumn_level_id = models.ManyToManyField(Level, through='PerevalLevel')


class Images(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(default='Moench_2339.jpg')
    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        with open('static/images', 'rb') as f:
            self.image.save(f)


class PerevalLevel(models.Model):
    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE)
    level_id = models.ForeignKey(Level, on_delete=models.CASCADE)
