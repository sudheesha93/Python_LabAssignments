import pandas as pd
import numpy as np

# declaring the data paths
data_path = 'C:/Users/sudheesha/Documents/GitHub/Python_LabAssignments/Lab3/Source/data/'
cust=pd.read_csv(data_path+'customers.csv')
cust_df = cust.iloc[:, [3, 4]].values

# cust_df=pd.get_dummies(cust_df)
# cust_df=cust_df.values
# importing the required packages

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pylab as pl

# Fitting a model to the dataset given
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 10)
ypred = kmeans.fit_predict(cust_df)


#PLOTTING the values
plt.scatter(cust_df[ypred == 0, 0], cust_df[ypred == 0, 1], s = 100, c = 'cyan', label = 'Clust1')
plt.scatter(cust_df[ypred == 1, 0], cust_df[ypred == 1, 1], s = 100, c = 'red', label = 'Clust2')
plt.scatter(cust_df[ypred == 2, 0], cust_df[ypred == 2, 1], s = 100, c = 'magenta', label = 'Clust3')
plt.scatter(cust_df[ypred == 3, 0], cust_df[ypred == 3, 1], s = 100, c = 'green', label = 'Clust4')
plt.scatter(cust_df[ypred == 4, 0], cust_df[ypred == 4, 1], s = 100, c = 'blue', label = 'Clust5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
