from myapp.models import Customer
from django.conf import settings

settings.configure(
    INSTALLED_APPS=['myapp'],
    # Other settings...
)

customer = Customer(
    AccountNumber='12345',
    FirstName='John',
    LastName='Doe',
    Email='john.doe@example.com',
    Phone='123-456-7890',
    Age=30,
    MemberSince='2022-01-01',
    Occupation='Software Engineer',
    Income=50000,
    MaritalStatus='Single',
    City='New York',
    Education='Bachelor',
    NumAccounts=1,
    AvgAccountValue=1000.00,
    AvgCreditRate=3.50,
    AvgInvestmentRate=5.00,
    NetWorth=50000.00,
    TotalLiabilities=10000.00,
    CreditScore=720,
    AccountActive=True,
)
customer.save()