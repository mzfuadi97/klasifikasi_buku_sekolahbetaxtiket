#!/bin/bash

# Set environment variables
export MLFLOW_TRACKING_URI=http://localhost:8080
export MLFLOW_TRACKING_NAME=book-classification

# Serve the model
mlflow models serve -m runs:/c10a9bc990534bc68c9ae3d67bc01d34/model -p 5000 --no-conda
