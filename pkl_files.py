import joblib

# Save your pipeline and label encoder
joblib.dump(best_model, "pesticide_predictor.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")
