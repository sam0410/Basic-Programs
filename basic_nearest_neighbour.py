from scipy.spatial import distance
def dist(a,b):
    return distance.euclidean(a,b)

class basicNN():

    def fit(self,X,y):
        self.X=X
        self.y=y
        return self

    def closest(self,row):
        bestIndex=0
        mindist=dist(row,self.X[0])
        for i in range(1, len(self.X)):
            tempdist=dist(self.X[i],row)
            if(tempdist<mindist):
                mindist=tempdist
                bestIndex=i
        return self.y[bestIndex]    

    def predict(self,X_test):
        predictions=[]
        for row in X_test:
            label=self.closest(row)
            predictions.append(label)
        return predictions
            
from sklearn.datasets import load_iris
iris=load_iris()
X=iris.data
y=iris.target

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.5)

#from sklearn import tree
#clf=tree.DecisionTreeClassifier()
clf=basicNN()
clf=clf.fit(X_train,y_train)
predictions= clf.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predictions))
