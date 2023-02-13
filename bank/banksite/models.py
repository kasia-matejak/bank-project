from django.db import models

class Account(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.IntegerField(default=0)

    def __int__(self):
        return self.number

class Transfer(models.Model):
    sender = models.ManyToManyField(Account, related_name='sender')
    receiver = models.ManyToManyField(Account, related_name='receiver')
    ammount = models.IntegerField()
    description = models.CharField(max_length=100)
    