import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from sklearn.metrics import roc_auc_score, roc_curve
import shap
from sklearn.model_selection import cross_val_score

def model_selection(X_train, y_train):
    # Initialize the models 
    dt = DecisionTreeClassifier(random_state=42)
    rf = RandomForestClassifier(random_state=42)

    # Evaluate the model using cross validation 
    scores_dt = cross_val_score(dt, X_train, y_train, cv=5)
    scores_rf = cross_val_score(rf, X_train, y_train, cv=5)

    print("Decision tree cross validation score:" (scores_dt).mean)
    print("Random Forest cross validation score:" (scores_rf).mean)

    return dt, rf