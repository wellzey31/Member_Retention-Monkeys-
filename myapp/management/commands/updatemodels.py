from django.core.management.base import BaseCommand
import pandas as pd
from myapp.models import Customer

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #Database Connections Here
        df = pd.read_csv('genData.csv')
        for ACCOUNTNUMBER, FIRSTNAME, LASTNAME, EMAIL, PHONE, AGE, MEMBERSINCE, OCCUPATION, INCOME, MARITALSTATUS, CITY, EDUCATION, NUMACCOUNTS, AVGACCOUNTVALUE, AVGCREDITRATE, AVGINVESTMENTRATE, NETWORTH, TOTALLIABILITIES, CREDITSCORE, ACCOUNTACTIVE in zip(df.AccountNumber, df.FirstName, df.LastName, df.Email, df.Phone, df.Age, df.MemberSince, df.Occupation, df.Income, df.MaritalStatus, df.City, df.Education, df.NumAccounts, df.AvgAccountValue, df.AvgCreditRate, df.AvgInvestmentRate, df.NetWorth, df.TotalLiabilities, df.CreditScore, df.AccountActive):
            models=Customer(AccountNumber=ACCOUNTNUMBER, FirstName=FIRSTNAME, LastName=LASTNAME, Email=EMAIL, Phone=PHONE, Age=AGE, MemberSince=MEMBERSINCE, Occupation=OCCUPATION, Income=INCOME, MaritalStatus=MARITALSTATUS, City=CITY, Education=EDUCATION, NumAccounts=NUMACCOUNTS, AvgAccountValue=AVGACCOUNTVALUE, AvgCreditRate=AVGCREDITRATE, AvgInvestmentRate=AVGINVESTMENTRATE, NetWorth=NETWORTH, TotalLiabilities=TOTALLIABILITIES, CreditScore=CREDITSCORE, AccountActive=ACCOUNTACTIVE)
            models.save()
