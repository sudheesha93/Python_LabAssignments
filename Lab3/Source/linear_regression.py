print(__doc__)

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the predict dataset
predict = datasets.load_boston()


# to load from url or csv files
# filename = 'Data/weather.csv'
# raw_data = open(filename, 'rt')
# reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
# x = list(reader)
# predict = numpy.array(x).astype('float')

predict_X = predict.data[:, np.newaxis, 2]

predict_X_train = predict_X[:-20]
predict_X_test = predict_X[-20:]

# Split the targets

# trainings
predict_y_train = predict.target[:-20]

# testings
predict_y_test = predict.target[-20:]

# linear regression object creation
regr = linear_model.LinearRegression()
regr.fit(predict_X_train, predict_y_train)
predict_y_pred = regr.predict(predict_X_test)

# The coefficients
print('Coeff: \n', regr.coef_)

# The mean squared error
print("Mean squared err: %.2f" % mean_squared_error(predict_y_test, predict_y_pred))

# Explained variance score: 1 is perfect prediction
print('Variance: %.2f' % r2_score(predict_y_test, predict_y_pred))

# output
plt.scatter(predict_X_test, predict_y_test, color='black')
plt.plot(predict_X_test, predict_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
