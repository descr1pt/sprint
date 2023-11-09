from django.contrib.auth.models import User
from django.core.files import File
from django.db import models


class Users(models.Model):
    autUser = models.OneToOneField(User, on_delete=models.CASCADE)
    mail = models.CharField(max_length=128, unique=True)
    full_name = models.CharField(max_length=128)
    phone = models.IntegerField(unique=True)

    # для удобного отображения на странице администратора
    def __str__(self):
        return self.autUser.username


class Coord(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    height = models.IntegerField()


class Images(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(default='Moench_2339.jpg')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        with open('static/images', 'rb') as f:
            self.image.save(f)


class PerevalAdded(models.Model):
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

    LEVEL_1 = '1A'
    LEVEL_2 = '1Б'
    LEVEL_3 = '2А'
    LEVEL_4 = '2Б'
    LEVEL_5 = '3А'
    LEVEL_6 = '3Б'
    LEVEL_CHOICES = (
        ('1А', '1А'),
        ('1Б', '1Б'),
        ('2А', '2А'),
        ('2Б', '2Б'),
        ('3А', '3А'),
        ('3Б', '3Б'),
    )
    beautyTitle = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    other_titles = models.CharField(max_length=128)
    connect = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True)
    coord_id = models.OneToOneField(Coord, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    photo_id = models.ManyToManyField(Images, through='PerevalImages')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NEW)
    winter_dif = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1)
    spring_dif = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1)
    summer_dif = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1)
    autumn_dif = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1)


class PerevalImages(models.Model):
    photo_id = models.ForeignKey(Images, on_delete=models.CASCADE)
    pereval_id = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
