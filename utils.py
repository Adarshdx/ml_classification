# Utility functions for the classification project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

def create_churn_data(n_samples=5000, save_path='data/telco_churn.csv'):
    """Generate synthetic churn dataset"""
    np.random.seed(42)
    
    data = {
        'tenure': np.random.randint(1, 72, n_samples),
        'monthly_charges': np.random.uniform(20, 120, n_samples),
        'total_charges': np.random.uniform(100, 8000, n_samples),
        'age': np.random.randint(18, 70, n_samples),
        'num_services': np.random.randint(1, 8, n_samples),
        'payment_delay_days': np.random.exponential(5, n_samples),
        'complaints': np.random.poisson(0.5, n_samples),
        'contract_monthly': np.random.choice([0,1], n_samples, p=[0.6,0.4]),
        'contract_yearly': np.random.choice([0,1], n_samples, p=[0.85,0.15]),
        'paperless_billing': np.random.choice([0,1], n_samples, p=[0.5,0.5]),
        'churn': np.random.choice([0,1], n_samples, p=[0.73,0.27])
    }
    
    df = pd.DataFrame(data)
    # Make churn more realistic
    df['churn'] = ((df['tenure'] < 12) & (df['monthly_charges'] > 60) | 
                   (df['payment_delay_days'] > 10) | 
                   (df['complaints'] > 2)).astype(int)
    
    df.to_csv(save_path, index=False)
    print(f"Data saved to {save_path}")
    return df

def plot_confusion_matrix(y_true, y_pred, title="Confusion Matrix"):
    """Plot confusion matrix"""
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['No Churn', 'Churn'],
                yticklabels=['No Churn', 'Churn'])
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.tight_layout()
    return plt

def print_detailed_report(y_test, y_pred, model_name):
    """Print detailed classification report"""
    print(f"\n{'='*50}")
    print(f"Detailed Report: {model_name}")
    print(f"{'='*50}")
    print(classification_report(y_test, y_pred, 
                                target_names=['No Churn', 'Churn']))

if __name__ == "__main__":
    # Test the utility functions
    df = create_churn_data(1000, 'data/test_data.csv')
    print("Utility functions ready!")
