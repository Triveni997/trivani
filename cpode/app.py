from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Route to serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the prediction logic
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    dataset_1 = request.form.get('dataset_1')
    dataset_2 = request.form.get('dataset_2')
    dataset_3 = request.form.get('dataset_3')
    dataset_4 = request.form.get('dataset_4')

    # Simulate prediction by generating random values
    prediction_1 = random.randint(1, 100)  # Random temperature quality score
    prediction_2 = random.uniform(0.1, 10.0)  # Random humidity quality score
    prediction_3 = random.choice(['Good', 'Moderate', 'Poor'])  # Random air quality status

    result = {
        'prediction_1': prediction_1,
        'prediction_2': prediction_2,
        'prediction_3': prediction_3
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
