from django.db import models

# Create your models here.
class Customer(models.Model):
    AccountNumber = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone = models.CharField(max_length=50)
    Age = models.PositiveIntegerField()
    Occupation = models.CharField(max_length=50)
    MaritalStatus = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Education = models.CharField(max_length=50)
    NumAccounts = models.PositiveIntegerField()
    AvgAccountValue = models.DecimalField(max_digits=10, decimal_places=2)
    AvgCreditRate = models.DecimalField(max_digits=5, decimal_places=2)
    AvgInvestmentRate = models.DecimalField(max_digits=5, decimal_places=2)
    NetWorth = models.DecimalField(max_digits=10, decimal_places=2)
    Income = models.PositiveIntegerField()
    TotalLiabilities = models.DecimalField(max_digits=10, decimal_places=2)
    CreditScore = models.PositiveIntegerField()
    MemberSince = models.DateField()
    AccountActive = models.BooleanField()
    Risk = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.FirstName



