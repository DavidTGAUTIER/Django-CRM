from django.db import models

# get migrations : 
# $ python manage.py makemigrations : create website\migrations\0001_initial.py 
# $ python manage.py migrate        : migrate the file to Mysql database

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone =  models.CharField(max_length=15)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")