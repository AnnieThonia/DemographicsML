# src/components/data_ingestion.py

from src.utils import load_data

def ingest_data(file_path):
    # Function to ingest data
    data = load_data(file_path)
    # Add data preprocessing steps if needed
    return data
