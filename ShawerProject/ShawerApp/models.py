from django.db import models

# Create your models here.
class counselor(models.Model):
    first_name=models.CharField(max_length=50,help_text="the name for counselor")
    last_name=models.CharField(max_length=50,help_text="the name for counselor")
    start_date=models.DateField()
    expertise_field=models.CharField(max_length=50)
    statment=models.TextField(max_length=240)
    image= models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return self.first_name+ " " +self.last_name