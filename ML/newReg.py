import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import sklearn as sk
from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn import metrics


### Training data is already split.
print("Clean Regression :)")
df_train = pd.read_csv('training.csv')
df_test = pd.read_csv('predict.csv')



print(df_train['AccountActive'].value_counts()/df_train.shape[0])

# Set class weights
w1 = len(df_train[df_train.AccountActive == 1]) / df_train.shape[0]
w1 = round(w1*100)
w2 = len(df_train[df_train.AccountActive == 0]) / df_train.shape[0]
w2 = round(w2*100)

print(w1)
print(w2)
w = {0:w1, 1:w2}


# Look at correlations between various variables
corrCards = df_train.corr()
sns.heatmap(corrCards, square=False, cmap='Oranges')
plt.savefig('trainCorr.png')
plt.show()
plt.clf()


### Clean Data
# Copy dataset into new DataFrame
df_pre1 = df_train.copy()
# Drop AccountNumber, Name and Email as it is useless here
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
# would split data here; already split but will split train / validation
# Split training data into validation set at 20% rate
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.20)



### LINEAR REG ###
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression(class_weight=w)
logreg.fit(X_train, y_train)


col_names = ["Phone","Age","NumAccounts","AvgAccountValue","AvgCreditRate","AvgInvestmentRate","NetWorth","Income","TotalLiabilities","CreditScore"]
# Dropped Cols:
# [AccountNumber,FirstName,LastName,Email,
#Occupation,MaritalStatus,City,Education,
#,MemberSince,AccountActive]


# Check predictions on validation
y_pred_val = logreg.predict(X_val)
acc = metrics.accuracy_score(y_val, y_pred_val)

print("Accuracy:",acc)
plt.clf()
cm = confusion_matrix(y_val, y_pred_val)

sns.heatmap(cm, annot=True, cmap='coolwarm')
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.savefig('cmTrainVal.png')
plt.show()

# metrics: false / true positive rates, auc (area under curve)
y_pred_proba_val = logreg.predict_proba(X_val)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_val, y_pred_proba_val)
auc = metrics.roc_auc_score(y_val, y_pred_proba_val)

plt.clf()
plt.plot(fpr, tpr, label="AUC"+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.savefig('ROC-AUC_val.png')
plt.show()



### NOW FOR REAL TESTING ###
### Repeat running predictions on testing set ### 


### Prepare Test Data
# Copy dataset into new DataFrame
df_pre2 = df_test.copy()
# Drop AccountNumber, Name and Email as it is useless here
df_pre2 = df_pre2.drop("AccountNumber", axis=1)
df_pre2 = df_pre2.drop("FirstName", axis=1)
df_pre2 = df_pre2.drop("LastName", axis=1)
df_pre2 = df_pre2.drop("Email", axis=1)

# Drop categorical vars for now
df_pre2 = df_pre2.drop("Occupation", axis=1)
df_pre2 = df_pre2.drop("MemberSince", axis=1)
df_pre2 = df_pre2.drop("MaritalStatus", axis=1)
df_pre2 = df_pre2.drop("City", axis=1)
df_pre2 = df_pre2.drop("Education", axis=1)


### ML ALGO ###

# drop predictor column ("AccountActive")
X_test = df_pre2.drop("AccountActive", axis=1)
y_test = df_pre2["AccountActive"]
# Would split the data here
# Testing data is 2% of total data currently created/available


# Run predictions on validation
y_pred = logreg.predict(X_test)
acc = metrics.accuracy_score(y_test, y_pred)

print("Accuracy:",acc)
plt.clf()
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, cmap='coolwarm')
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.savefig('cmReal.png')
plt.show()

# metrics: false / true positive rates, auc (area under curve)
y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test, y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)

plt.clf()
plt.plot(fpr, tpr, label="AUC"+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.savefig('ROC-AUC_Real.png')
plt.show()


### list in order of probabilities
y_pred_proba = logreg.predict_proba(X_test)[::, 0]
newTest = pd.DataFrame(df_test)

y_pred_proba = y_pred_proba.tolist()
newTest['Predicted Values'] = y_pred_proba

newTest.to_csv('out.csv', index=False)
print(sorted(y_pred_proba, reverse=True))
