from django.db import models


class attsheet(models.Model):
    name=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=10)
    room_no=models.IntegerField()
    from_date=models.DateField()
    to_date=models.DateField()
    purpose=models.TextField(max_length=500)


    def __str__(self):
        return self.name+"'s"+'entry'

