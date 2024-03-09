# src/pipeline/train_pipeline.py

from src.components.data_ingestion import ingest_data
from src.components.data_transformation import transform_data
from src.components.model_trainer import train_model

def run_train_pipeline(data_file):
    # Ingest data
    data = ingest_data(data_file)
    # Transform data
    transformed_data = transform_data(data)
    # Train model
    trained_model = train_model(transformed_data)
    return trained_model
