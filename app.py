from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.predict_model import ChurnPredictor
from src.visualization.visualize import generate_dashboard_plots

app = Flask(__name__)

# Load model
model_path = os.path.join('models', 'random_forest.pkl')
if os.path.exists(model_path):
    predictor = ChurnPredictor(model_path)
else:
    predictor = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Make single prediction"""
    try:
        data = request.json
        prediction = predictor.predict(data)
        return jsonify({
            'success': True,
            'prediction': int(prediction['prediction']),
            'probability': float(prediction['probability']),
            'risk_level': prediction['risk_level']
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/batch-predict', methods=['POST'])
def batch_predict():
    """Make batch predictions from CSV"""
    try:
        file = request.files['file']
        df = pd.read_csv(file)
        predictions = predictor.predict_batch(df)
        return jsonify({
            'success': True,
            'predictions': predictions.tolist(),
            'summary': {
                'total': len(predictions),
                'churn_risk': int(predictions.sum()),
                'churn_rate': float(predictions.mean())
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/metrics')
def get_metrics():
    """Get model performance metrics"""
    metrics_path = os.path.join('reports', 'model_metrics.json')
    if os.path.exists(metrics_path):
        import json
        with open(metrics_path, 'r') as f:
            metrics = json.load(f)
        return jsonify(metrics)
    return jsonify({'error': 'Metrics not found'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
