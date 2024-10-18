from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Load the model
model = joblib.load('xgb_model.pkl')

# Load the scaler
scaler = joblib.load('scaler.pkl')

neighbourhood_mapping = joblib.load('neighbourhood_mapping.pkl')

# Load the feature columns
feature_columns = joblib.load('feature_columns.pkl')


# If you have encoders, load them as well
# encoder = joblib.load('encoder.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json(force=True)
        
        # Convert data to DataFrame
        input_df = pd.DataFrame([data])
        
        # Preprocess the input data
        preprocessed_df = preprocess_input(input_df)
        
        # Make prediction
        prediction_log_price = model.predict(preprocessed_df)
        prediction_price = np.expm1(prediction_log_price)  # Convert log price to original scale
        
        # Prepare response
        output = {
            'predicted_price': float(prediction_price[0])
        }
        return jsonify(output)
    
    except Exception as e:
        return jsonify({'error': str(e)})

def preprocess_input(df):
    # Encode 'room_type'
    room_type_mapping = {
        'Entire home/apt': [0, 0],
        'Private room': [1, 0],
        'Shared room': [0, 1]
    }
    room_type = df['room_type'].iloc[0]
    df['room_type_Private room'], df['room_type_Shared room'] = room_type_mapping.get(room_type, [0, 0])
    df.drop('room_type', axis=1, inplace=True)

    # Encode 'neighbourhood_group' using one-hot encoding
    neighbourhood_groups = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
    for ng in neighbourhood_groups:
        column_name = f'neighbourhood_group_{ng}'
        df[column_name] = 1 if df['neighbourhood_group'].iloc[0] == ng else 0
    df.drop('neighbourhood_group', axis=1, inplace=True)

    # Encode 'neighbourhood' using the same encoding as during training
    # Assuming you have a mapping of neighbourhood to encoded values
    # Load the mapping
    neighbourhood_mapping = joblib.load('neighbourhood_mapping.pkl')
    df['neighbourhood_encoded'] = df['neighbourhood'].map(neighbourhood_mapping)
    df.drop('neighbourhood', axis=1, inplace=True)

    # Scale numerical features
    numerical_features = ['latitude', 'longitude', 'minimum_nights', 'number_of_reviews',
                          'reviews_per_month', 'calculated_host_listings_count', 'availability_365']
    df[numerical_features] = scaler.transform(df[numerical_features])

    # Ensure the DataFrame has the correct columns in the correct order
    feature_order = ['latitude', 'longitude', 'minimum_nights', 'number_of_reviews',
                     'reviews_per_month', 'calculated_host_listings_count', 'availability_365',
                     'has_reviews', 'neighbourhood_encoded',
                     'neighbourhood_group_Brooklyn', 'neighbourhood_group_Manhattan',
                     'neighbourhood_group_Queens', 'neighbourhood_group_Staten Island',
                     'room_type_Private room', 'room_type_Shared room']
    df = df.reindex(columns=feature_columns, fill_value=0)

    return df



if __name__ == '__main__':
    app.run(debug=True, port=5001)
