from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import joblib

def train_model(X, y, test_size=0.2, random_state=42):
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=test_size, 
                                                        random_state=random_state)
    
    model = GradientBoostingRegressor(n_estimators=100, random_state=random_state)
    model.fit(X_train, y_train.values.ravel())
    
    return model, X_train, X_test, y_train, y_test

def save_model(model, path='../src/models/gradient_boosting_model.pkl'):
    joblib.dump(model, path)
