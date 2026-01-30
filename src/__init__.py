
"""
Customer Churn Prediction Package

This package implements a production-grade machine learning pipeline for
predicting customer churn in subscription-based businesses.

Design principles:
- Clear separation of data processing, feature engineering, training,
  evaluation, and inference
- Reusable preprocessing and modeling pipelines
- Single source of truth for inference logic
- Future-ready for FastAPI deployment, Streamlit dashboards,
  and uplift modeling extensions

Modules:
- data_preprocessing: Data loading, cleaning, and splitting
- feature_engineering: Feature transformation pipelines
- train: Model training and artifact persistence
- evaluate: Model evaluation and metrics reporting
- predict: Centralized inference logic
"""

