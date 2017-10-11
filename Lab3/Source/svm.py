import pandas as pd
from sklearn.svm import SVC
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split

#mnist = fetch_mldata('MNIST original', data_home=data_path)
data_path = 'C:/Users/sudheesha/Documents/GitHub/Python_LabAssignments/Lab3/Source/data/'
mnist=pd.read_csv(data_path+'mnist.csv')
mnist=mnist.values
mnist=mnist[:5000]

mnist_target=mnist[:,0]
mnist_data=mnist[:,1:]

# splitting the dataset into train and test
X_train,X_test,y_train,y_test=train_test_split(mnist_data,mnist_target,test_size=0.20,random_state=0)

# fitting the linear model
svm_lin=SVC(kernel='linear')
svm_lin.fit(X_train,y_train)
preds_lin=svm_lin.predict(X_test)
x=metrics.accuracy_score(y_test, preds_lin)
print('Accuracy by using the linear kernel on the data')
print("A={}".format(metrics.accuracy_score(y_test, preds_lin)))

# fitting the rbf model
svm_rbf=SVC(kernel='rbf')

svm_rbf.fit(X_train,y_train)

preds_rbf=svm_rbf.predict(X_test)
y=metrics.accuracy_score(y_test, preds_rbf)
print('Accuracy by using the RBF kernel on the data')
print("A={}".format(metrics.accuracy_score(y_test, preds_rbf)))

if x>y:
    print("Linear Kernal gives us the highest accuracy when compared to RBF")
else:
    print("Linear Kernal gives us the lowest accuracy when compared to RBF")




"""
Use linear kernel when number of features is larger than number of observations.
Use gaussian kernel when number of observations is larger than number of features.
If number of observations is larger than 50,000 speed could be an issue when using gaussian kernel; hence, one might want to use linear kernel.

so here, linear is giving you better accuracy than the rbf

"""