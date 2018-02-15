# For classification

from scipy.spatial import distance

def dist(a,b):
    return distance.euclidean(a,b)

def splitIndexWise(index,value,dataset):
    left,right=list(),list()
    for row in dataset:
        if(row[index]<value):
            right.append(row)
        else:
            left.append(row)
    return left,right

def giniIndex(groups,labels):
    gini=0.0
    totalSize= float(sum([len(group) for group in groups]))
    for group in groups:
        n=len(group)
        labelsInGroup= [row[-1] for row in group]
        temp=n/totalSize
        if (n== 0):
            continue
        for label in labels :
            temp*= (labelsInGroup.count(label)/n)
        gini+=temp
        return gini
            
    

def getSplit(dataset):
    labels= list(set(row[-1] for row in dataset))
    n= len(dataset[0])-1
    BestGini,BestIndex,BestGroups=-1,-1,None
    for row in dataset:
        for i in range(n) : 
            groups=splitIndexWise(i,row[i],dataset)
            gini= giniIndex(groups,labels)
            if(gini>BestGini):
                BestGini,BestIndex,BestGroups=gini,i,groups
    return {'index':BestIndex,'groups':BestGroups,'gini':BestGini}


from sklearn.datasets import load_iris
iris= load_iris()
X=iris.data
y=iris.target


dataset = [[2.771244718,1.784783929,0],
	[1.728571309,1.169761413,0],
	[3.678319846,2.81281357,0],
	[3.961043357,2.61995032,0],
	[2.999208922,2.209014212,0],
	[7.497545867,3.162953546,1],
	[9.00220326,3.339047188,1],
	[7.444542326,0.476683375,1],
	[10.12493903,3.234550982,1],
	[6.642287351,3.319983761,1]]
split = getSplit(dataset)
'''import numpy as np
y=y[:,None]                         #To convert array of size (150,) to size (150,1)
np.concatenate((X,y),axis=1)
split= getSplit(X)'''
