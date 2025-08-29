import joblib

def load_model(path):
    return joblib.load(path)

def predict(model, country):
    # Dummy example, replace with real feature extraction
    if country == "all":
        return {"value": 123.4}
    return {"value": 56.7}

def train_model(X, y, save_path="models/model_v1.pkl"):
    from sklearn.linear_model import LinearRegression
    model = LinearRegression().fit(X, y)
    joblib.dump(model, save_path)
    return model
