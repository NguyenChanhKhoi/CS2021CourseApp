from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass


#tao class ke thua
class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Catergory(BaseModel):
    name = models.CharField(max_length = 50, null = False)


    def __str__ (self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length= 255, null = False)
    description = models.TextField()
    created_date = models.DateField(auto_now_add= True)
    update_date = models.DateField(auto_now= True)
    active = models.BooleanField(default = True)
    image = models. CharField(max_length= 100)
    category = models.ForeignKey(Catergory, on_delete= models.CASCADE)

    def __str__(self):
        return self.subject