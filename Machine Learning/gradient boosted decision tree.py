from sklearn.datasets import load_iris
iris= load_iris()
X=iris.data
y=iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.4)

from sklearn.ensemble import GradientBoostingClassifier

clf= GradientBoostingClassifier().fit(X_train,y_train)

print(clf.score(X_test,y_test))

