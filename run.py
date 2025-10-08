import pandas as pd
import numpy as np
import joblib as jl
import argparse

def clean_input_data(df, expected_columns):
    # Create a copy for preprocessing
    df_clean = df.copy()

    # Replace '?' cells with NaN values
    df_clean = df_clean.replace('?', np.nan)

    # Replace non-numeric diag_* values with NaN
    for col in ['diag_1', 'diag_2', 'diag_3', 'diag_4', 'diag_5']:
        df_clean[col] = pd.to_numeric(df_clean[col].apply(lambda v: v if str(v)[0].isnumeric() else np.nan))

    # Parse X1 and X2 columns to make them numerical
    def parse_dosage(value):
        if pd.isna(value):
            return 0
        elif isinstance(value, str) and value.startswith('>'):
            try:
                return float(value[1:])
            except ValueError:
                return np.nan
        elif isinstance(value, float):
            return value
        else:
            return np.nan

    for col in ['X1', 'X2']:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].apply(parse_dosage)

    # Drop unnecessary columns, and ensure all expected ones are present
    available_columns = [col for col in expected_columns if col in df_clean.columns]
    missing_columns = [col for col in expected_columns if col not in df_clean.columns]
    if missing_columns:
        print(f"[ERROR]: Missing some of the expected columns in training dataset: {missing_columns}")
        exit(1)
    df_clean = df_clean[available_columns]

    # Drop incomplete rows (rows with any NaN values)
    df_clean = df_clean.dropna()

    return df_clean


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Hospital Readmission Predictor")
    parser.add_argument('--input', type=str, required=True, help="Path to input CSV file")
    parser.add_argument('--output', type=str, required=True, help="Path to output CSV file")
    parser.add_argument('--model', type=str, default="model_pipeline.joblib",
                        help="Path to the trained model pipeline file (defaults to ./model_pipeline.joblib)")

    args = parser.parse_args()

    print(f"Loading model pipeline from {args.model}")
    artifacts = jl.load(args.model)
    model = artifacts['pipeline']

    print(f"Model loaded successfully!")
    print(f"Model type: {artifacts.get('model_type')}")
    print(f"Training accuracy: {artifacts.get('training_accuracy')*100:.2f}%")
    print(f"Validation accuracy: {artifacts.get('validation_accuracy')*100:.2f}%")
    print(f"Model created at: {artifacts.get('created_at')}")

    # Load input data
    print(f"\nLoading input data from: {args.input}")
    input_df = pd.read_csv(args.input)
    print(f"Input data shape: {input_df.shape}")

    # Store encounter_ids for output
    encounter_ids = input_df['encounter_id'].copy()

    # Clean input data
    input_df = clean_input_data(input_df, artifacts.get('feature_names'))
    if len(input_df) == 0:
        print("[ERROR]: No valid rows found in input data after cleaning.")
        exit(1)
    else:
        print(f"Cleaned input data shape: {input_df.shape}")

    # Generate predictions
    predictions = model.predict(input_df)
    output_df = pd.DataFrame()
    output_df['encounter_id'] = encounter_ids.loc[input_df.index]
    output_df['readmitted_prediction'] = predictions

    # Save predictions to output CSV file
    output_df.to_csv(args.output, index=False)
    print(f"\nPredictions saved successfully to {args.output}")
