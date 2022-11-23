from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from PIL import Image

# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'W', '여성'

    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    lovings = models.ManyToManyField('self', symmetrical=False, related_name='lovers')
    favorite = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(choices=GenderChoices.choices, max_length=1, blank=True)
    phone_number = models.CharField(validators=[RegexValidator(r'010-?[1-9]\d{3}-?\d{4}$')], max_length=13, blank=True)
    self_introduce = models.TextField(null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='sample.png', upload_to='static')

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)