from django.contrib.auth.models import AbstractUser
from django.db import models
from SGC.settings import MEDIA_URL, STATIC_URL
# Create your models here.


class User (AbstractUser):
    imagen = models.ImageField(upload_to='cheque/%Y/%m/%d', null=True, blank=True)

    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        else:
            return '{}{}'.format(STATIC_URL, 'img/empty.png')
