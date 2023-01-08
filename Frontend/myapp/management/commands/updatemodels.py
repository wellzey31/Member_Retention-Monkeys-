from django.core.management.base import BaseCommand
import pandas as pd
from myapp.models import Customer

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Customer.objects.all().delete()

        #Database Connections Here
        df = pd.read_csv('genData.csv')
        for ACCOUNTNUMBER, FIRSTNAME, LASTNAME, EMAIL, PHONE, AGE, OCCUPATION, MARITALSTATUS, CITY, EDUCATION, NUMACCOUNTS, AVGACCOUNTVALUE, AVGCREDITRATE, AVGINVESTMENTRATE, NETWORTH, INCOME, TOTALLIABILITIES, CREDITSCORE, MEMBERSINCE, ACCOUNTACTIVE, PREDICTEDVALUE in zip(df.AccountNumber, df.FirstName, df.LastName, df.Email, df.Phone, df.Age, df.Occupation, df.MaritalStatus, df.City, df.Education, df.NumAccounts, df.AvgAccountValue, df.AvgCreditRate, df.AvgInvestmentRate, df.NetWorth, df.Income, df.TotalLiabilities, df.CreditScore, df.MemberSince, df.AccountActive, df.PredictedValues):
            models=Customer(AccountNumber=ACCOUNTNUMBER, FirstName=FIRSTNAME, LastName=LASTNAME, Email=EMAIL, Phone=PHONE, Age=AGE, MemberSince=MEMBERSINCE, Occupation=OCCUPATION, Income=INCOME, MaritalStatus=MARITALSTATUS, City=CITY, Education=EDUCATION, NumAccounts=NUMACCOUNTS, AvgAccountValue=AVGACCOUNTVALUE, AvgCreditRate=AVGCREDITRATE, AvgInvestmentRate=AVGINVESTMENTRATE, NetWorth=NETWORTH, TotalLiabilities=TOTALLIABILITIES, CreditScore=CREDITSCORE, AccountActive=ACCOUNTACTIVE, Risk=PREDICTEDVALUE*100)
            models.save()
