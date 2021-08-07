import numpy as np
import pandas as pd
import piskle
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('HW4.csv')

features = df.iloc[:, [2,3,4,5,6,7,8]].values
predict = df.iloc[:, 1].values

fTrain, fTest, pTrain, pTest = train_test_split(features, predict, test_size = 0.5, random_state = 0)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
classifier.fit(fTrain, pTrain)

# Predicting the test set results

predicted = classifier.predict(fTest)

# Making the Confusion Matrix

cm = confusion_matrix(pTest, predicted)
print(cm)

piskle.dump(classifier, 'randomForestClassifier.pskl', optimize=False)