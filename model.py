# Regular Exploratory Data Analysis and plotting libraries
import pandas as pd
import numpy as np
import pickle

# Models from Scikit Learn
from sklearn.linear_model import LogisticRegression

# Model evaluation
from sklearn.model_selection import train_test_split

data = pd.read_csv("heart-disease.csv")

# Modelling
np.random.seed(42)
# Split data into X and y
X = data.drop("target", axis=1)
y = data["target"]

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(max_iter=100)
# Fit the model to data
model.fit(X_train, y_train)
# Evaluate model and append its score
model.score(X_test, y_test)

# save model
pickle.dump(model, open('logistic_regression_model.pkl', 'wb'))
model = pickle.load(open('logistic_regression_model.pkl', 'rb'))