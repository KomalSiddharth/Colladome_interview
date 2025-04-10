# Iris Classification (Scikit-learn) Using scikit-learn, write Python code to: Load the Iris dataset
# Train a Logistic Regression model
# Print the accuracy score of the model on a test split

# imported the required libraries 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
# import the dataset
# data=pd.read_csv('iris.csv')
# print(data).head(5)
# load the data from the dataset
data=load_iris()
X=data.data
y=data.target
# split the training dataset into training and testing dataset
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=50)
log_reg=LogisticRegression()
# train the models
log_reg.fit(X_train,y_train)
# make predictions
ypred_1=log_reg.predict(X_test)
# lets check the accuracy of both the models
accuracy_1=accuracy_score(y_test,ypred_1)
print("Accuracy of logistic regression: ",accuracy_1)


