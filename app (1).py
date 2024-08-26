from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import joblib
import dill
import pandas as pd

app = Flask(__name__)

# Load the model and preprocessor
preprocessor = joblib.load('preprocessor1.pkl')
model = tf.keras.models.load_model('Final1.keras')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from the JSON request
        data = request.json

        # Check if all required fields are provided
        required_fields = ['height', 'weight', 'waist', 'hip', 'bust', 'gender', 'Cup_Size']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing field: {field}")

        height = float(data['height'])
        weight = int(data['weight'])
        waist = int(data['waist'])
        hip = int(data['hip'])
        bust = int(data['bust'])
        gender = data['gender']
        cup_size = data['Cup_Size']

        # Create a DataFrame for the input data
        input_data = pd.DataFrame({
            'Height': [height],
            'Weight': [weight],
            'Bust/Chest': [bust],
            'Waist': [waist],
            'Hips': [hip],
            'Cup Size': [cup_size],
            'Gender': [gender],
        })

        # Preprocess the input data
        preprocessed_data = preprocessor.transform(input_data)

        # Call the model with the preprocessed data
        size_prediction = model.predict(preprocessed_data)
        size_prediction = size_prediction[0][0].item()  # Ensure size_prediction is a scalar value

        return jsonify({'size': size_prediction})
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
