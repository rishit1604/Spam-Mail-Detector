import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load data
raw_mail_data = pd.read_csv('C:/Users/HP/Desktop/ML/Spam_Mail_Predictor/model-training/emails.csv')
mail_data = raw_mail_data.where(pd.notnull(raw_mail_data), '')

X = mail_data['text']
Y = mail_data['spam']

#Split data in train and test data
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

#Convert string to vector
feature_extraction = TfidfVectorizer(min_df=1,stop_words='english',lowercase=True)

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

#Logistic regression
LRmodel = LogisticRegression()
LRmodel.fit(X_train_features,Y_train)

prediction_on_training_data = LRmodel.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train,prediction_on_training_data)
print('Logistic Regression Training Accuracy',accuracy_on_training_data)

prediction_on_testing_data = LRmodel.predict(X_test_features)
accuracy_on_testing_data = accuracy_score(Y_test,prediction_on_testing_data)
print('Logistic Regression Testing Accuracy',accuracy_on_testing_data)

# Naive Bayes classifier
NBmodel = MultinomialNB()  
NBmodel.fit(X_train_features, Y_train)

prediction_on_training_data = NBmodel.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)
print('Naive Bayes Training Accuracy:', accuracy_on_training_data)

prediction_on_testing_data = NBmodel.predict(X_test_features)
accuracy_on_testing_data = accuracy_score(Y_test, prediction_on_testing_data)
print('Naive Bayes Testing Accuracy:', accuracy_on_testing_data)

#SVM
SVMmodel = SVC()
SVMmodel.fit(X_train_features,Y_train)

prediction_on_training_data = SVMmodel.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train,prediction_on_training_data)
print('SVM training Accuracy',accuracy_on_training_data)

prediction_on_testing_data = SVMmodel.predict(X_test_features)
accuracy_on_testing_data = accuracy_score(Y_test,prediction_on_testing_data)
print('SVM Testing Accuracy',accuracy_on_testing_data)

 

import joblib
joblib.dump(LRmodel, 'logistic_model.pkl')
joblib.dump(NBmodel, 'naive_bayes_model.pkl')
joblib.dump(SVMmodel, 'svm_model.pkl')
joblib.dump(feature_extraction, 'vectorizer.pkl')
