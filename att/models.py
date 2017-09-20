from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator


class attsheet(models.Model):
    name=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=10)
    room_no=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(25)])
    from_date=models.DateField()
    to_date=models.DateField()
    purpose=models.TextField(max_length=500)
    approved=models.BooleanField(default=False)

    def __str__(self):
        return self.name+"'s"+' leave entry'

