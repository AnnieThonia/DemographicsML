# src/components/model_trainer.py

from src.utils import save_model

def train_model(data):
    # Function to train a machine learning model
    # Add model training code here
    model = None  # Placeholder for trained model
    # Save the trained model to a file
    save_model(model, 'trained_model.pkl')
    return model
