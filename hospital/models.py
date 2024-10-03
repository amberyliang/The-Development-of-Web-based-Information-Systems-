from django.db import models
from django.utils import timezone



# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.title

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
    	return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='static/image/')
    bio = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
    	return self.name

class Registration(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    id_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    DEPARTMENTS = (
        ('小兒科','小兒科'),
        ('婦產科','婦產科'),
        ('外科','外科'),
        ('內科','內科'),
        )
    date = models.DateTimeField(default = timezone.now)
    department = models.CharField(max_length=10, choices = DEPARTMENTS ,default = '小兒科')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('-date',)

class Emailreceive(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    id_number = models.CharField(max_length=10,default="a100000000")
    birthday = models.DateField(default='1990-01-01')
    phone_number = models.CharField(max_length=10,default='0900000000')
    password = models.CharField(max_length=20)
    superior = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    DEPARTMENTS = (
        ('小兒科','小兒科'),
        ('婦產科','婦產科'),
        ('外科','外科'),
        ('內科','內科'),
        )
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    date = models.DateTimeField(default = timezone.now)
    department = models.CharField(max_length=10, choices = DEPARTMENTS)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date',)

