import random
import numpy as np


sigma=1
lenInput=5000
u= np.array([int(random.choice([False, True])) for i in range(lenInput)])
u= u*2 -1
M= 9 #amount of delay (number of features)


x=np.array([u[i]+0.5*u[i-1] if i>0 else 0 for i in range(lenInput)])
y=np.array([ x[i]- 0.9*pow(x[i],3) for i in range(lenInput)])
noise=np.random.normal(0, sigma, lenInput)
output= y+noise


u=u[:,None]


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test=train_test_split(output,u, test_size=0.4)


XTrain_features=np.array([X_train[i-M+1:i+1] for i in range(M-1,len(X_train))])
XTest_features=np.array([X_test[i-M+1:i+1] for i in range(M-1,len(X_test))])

y_train=y_train.ravel();
y_test=y_test.ravel();

from sklearn import tree
from sklearn import svm
#y_train= y_train[:,None]
clfsvm = svm.SVC()
clfsvm.fit(XTrain_features, y_train[M-1:])

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import linear_model
from sklearn.ensemble import BaggingClassifier
'''
clfADAforest = AdaBoostRegressor(RandomForestRegressor(max_depth=2))
clfADAdt = AdaBoostRegressor(tree.DecisionTreeRegressor(max_depth=2))
clf=RandomForestRegressor(max_depth=2)
clfdt=tree.DecisionTreeRegressor(max_depth=2)
'''

clfADAforest = AdaBoostClassifier(RandomForestClassifier())
clfADAdt = AdaBoostClassifier(tree.DecisionTreeClassifier())

clfGB = GradientBoostingClassifier()

clf=RandomForestClassifier()
clfdt=tree.DecisionTreeClassifier()
clflogistic = linear_model.LogisticRegression()
clfDTbagging = BaggingClassifier(base_estimator=tree.DecisionTreeClassifier())

clf.fit(XTrain_features, y_train[M-1:])
clfADAforest.fit(XTrain_features, y_train[M-1:])
clfADAdt.fit(XTrain_features, y_train[M-1:])
clfGB.fit(XTrain_features, y_train[M-1:])
clfdt.fit(XTrain_features, y_train[M-1:])
clflogistic.fit(XTrain_features, y_train[M-1:])
clfDTbagging.fit(XTrain_features, y_train[M-1:])
test_check=y_test[M-1:];
test_check_size= len(test_check)

pp= clfsvm.predict(XTest_features)
print("SVM Score: ",sum(test_check==pp)/test_check_size)

pp=clfdt.predict(XTest_features)
print("Decision Tree Score: ",sum(test_check==pp)/test_check_size)



pp=clf.predict(XTest_features)
print("Random Forest Score: ",sum(test_check==pp)/test_check_size)

pp=clfADAdt.predict(XTest_features)
print("ADA Boosted Decision Tree Score: ",sum(test_check==pp)/test_check_size)

pp=clfADAforest.predict(XTest_features)
print("ADA Boosted Random Forest Score: ",sum(test_check==pp)/test_check_size)


pp=clfGB.predict(XTest_features)
print("Gradient Boosted Decision Tree Score: ",sum(test_check==pp)/test_check_size)




pp=clflogistic.predict(XTest_features)
print("Logistic Regression Score: ",sum(test_check==pp)/test_check_size)

pp=clfDTbagging.predict(XTest_features)
print("Bagged Decision Tree Score: ",sum(test_check==pp)/test_check_size)
