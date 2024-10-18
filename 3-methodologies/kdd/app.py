from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('optimized_random_forest_model.joblib')
scaler = joblib.load('scaler.joblib')  # Assuming you saved the scaler during preprocessing

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = data['features']
    
    # Extract feature values
    feature_values = [
        features['fixed_acidity'],
        features['volatile_acidity'],
        features['citric_acid'],
        features['residual_sugar'],
        features['chlorides'],
        features['free_sulfur_dioxide'],
        features['total_sulfur_dioxide'],
        features['density'],
        features['pH'],
        features['sulphates'],
        features['alcohol']
    ]
    
    # Compute density_diff
    density_diff = features['density'] - (features['alcohol'] * 0.01)
    feature_values.append(density_diff)
    
    # Convert to numpy array and reshape
    input_features = np.array(feature_values).reshape(1, -1)
    
    # Apply scaling
    input_features_scaled = scaler.transform(input_features)
    
    # Make prediction
    prediction = model.predict(input_features_scaled)
    output = {'prediction': int(prediction[0])}
    
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
