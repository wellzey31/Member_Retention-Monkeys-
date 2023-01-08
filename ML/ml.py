import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import metrics

print("Hello")
df_card = pd.read_csv('genData4.csv')
print(df_card.head())

# Look at correlations between various variables
corrCards = df_card.corr()
sns.heatmap(corrCards, square=False, cmap='Oranges')
plt.savefig('corr.png')
plt.show()

print(corrCards)
print(corrCards.values)

### Sort the variables and display the highest correlations
absCorrs = corrCards.abs()
corrsList = absCorrs.unstack()
sortedCorrs = corrsList.sort_values(kind="quicksort")
print(sortedCorrs[:])

# for i in range(len(corrCards)):
#     print(corrCards[i])

# for index, row in corrCards.iterrows():
#     print(index)
#     print(isinstance(row, float))
#     if(isinstance(row, float) and abs(i) > 0.80):
#         print(row)

print("==== High Correlations ====")
print("__")

# Clean Data

# Copy dataset into new DataFrame
df_pre1 = df_card.copy()
# Drop AccountNumber as it is useless here
df_pre1 = df_pre1.drop("AccountNumber", axis=1)
df_pre1 = df_pre1.drop("FirstName", axis=1)
df_pre1 = df_pre1.drop("LastName", axis=1)
df_pre1 = df_pre1.drop("Email", axis=1)

# Drop categorical vars for now
df_pre1 = df_pre1.drop("Occupation", axis=1)
df_pre1 = df_pre1.drop("MemberSince", axis=1)
df_pre1 = df_pre1.drop("MaritalStatus", axis=1)
df_pre1 = df_pre1.drop("City", axis=1)
df_pre1 = df_pre1.drop("Education", axis=1)


### ML ALGO ###

# drop predictor column ("AccountActive")
X = df_pre1.drop("AccountActive", axis=1)
y = df_pre1["AccountActive"]

# Split Training and Testing data sets at 20% rate
X_train_all, X_test, y_train_all, y_test = train_test_split(X, y, test_size=0.20)
# Split training data into validation set
X_train, X_val, y_train, y_val = train_test_split(X_train_all, y_train_all, test_size=0.20)



### DECISION TREE ###
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
# from dtreeviz.trees import dtreeviz

classifier = DecisionTreeClassifier(max_depth=10)
classifier.fit(X_train, y_train)

col_names = ["Phone","Age","NumAccounts","AvgAccountValue","AvgCreditRate","AvgInvestmentRate","NetWorth","Income","TotalLiabilities","CreditScore"]
# Removed classes / variables:
#[AccountNumber,FirstName,LastName,Email,
#Occupation,MaritalStatus,City,Education,
#,MemberSince,AccountActive]


tree.plot_tree(classifier,
               feature_names=col_names,
               class_names={0:'Not', 1:'Active'},
               filled = True)
plt.savefig('tree.png', dpi=200)
plt.show()

# viz = dtreeviz(classifier, X_train, y_train,
#                target_name="AccountActive",
#                feature_names=X_train.columns.to_list(),
#                class_names={0:'Not',1:'Active'})


# diagram = viz.view()
# diagram.show()
# diagram.save("cards.svg")

print(X_test)
print(X_test.shape)
# All categories:
# [AccountNumber,FirstName,LastName,Email,Phone,Age,Occupation,MaritalStatus,City,
# Education,NumAccounts,AvgAccountValue,AvgCreditRate,AvgInvestmentRate,NetWorth,Income,
# TotalLiabilities,CreditScore,MemberSince,AccountActive]


y_pred = classifier.predict(X_test)
print(y_pred)
acc = metrics.accuracy_score(y_test, y_pred)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
plt.clf()
cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, cmap='coolwarm')
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.savefig('cm.png')
plt.show()

## SAVING MODEL
import pickle
## CHECK IF MODEL ACC EXISTS
file = open('model2', 'rb')
classifier2 = pickle.load(file)
y_pred2 = classifier2.predict(X_test)
acc2 = metrics.accuracy_score(y_test, y_pred2)
file.close()
if(acc >= acc2):
    ## SAVE MODEL
    print("model overwritten")
    file = open('model2', 'wb')
    save = pickle.dump(classifier, file)
    file.close()
print("here")
print(y_pred2)
print("ACC 2:", acc2)



# Single Data Point Predictions

abc = [1907168620,"Spencer","Burgess","Spencer.Burgess642@monkeymail.com",4145995277,32,"Butcher","MARRIED","Vauxhall","NONE",1,148425.06,5.92,9.80,834618.09,99359.30,122572.05,589]
xyz = [822952702,"Jillian","Connolly","Jillian.Connolly677@monkeymail.com",4489932738,48,"Scaler","WIDOWED","Slave Lake","HIGHSCHOOL",2,928648.88,31.81,1.58,2018362.08,112131.23,188623.59,678]
# xyz :,2008-25-07
# abc : 2022-28-10
del abc[6:10]
del abc[0:4]
abc = [abc]
del xyz[6:10]
del xyz[0:4]
xyz = [xyz]
abc_pred = classifier.predict(abc)
print(abc_pred)
print(int(abc_pred))

xyz_pred = classifier.predict(xyz)
print(xyz_pred)
print(int(xyz_pred))

        