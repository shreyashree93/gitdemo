# preprocess.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os

def preprocess_data():
    # Load the dataset
    data_path = os.path.join('data', 'restaurant_data.csv')  # adjust if needed
    data = pd.read_csv(data_path)

    print("Initial data shape:", data.shape)

    # Drop rows with missing values
    data.dropna(inplace=True)
    print("After dropping missing values:", data.shape)

    # Encode categorical columns
    categorical_cols = ['City', 'Cuisines', 'Restaurant Type']  # adjust based on your dataset
    le = LabelEncoder()
    for col in categorical_cols:
        if col in data.columns:
            data[col] = le.fit_transform(data[col])

    # Separate features and target
    if 'Aggregate rating' not in data.columns:
        raise ValueError("Column 'Aggregate rating' is required as target.")

    X = data.drop('Aggregate rating', axis=1)
    y = data['Aggregate rating']

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Save preprocessed data to CSV files for reuse
    X_train.to_csv('X_train.csv', index=False)
    X_test.to_csv('X_test.csv', index=False)
    y_train.to_csv('y_train.csv', index=False)
    y_test.to_csv('y_test.csv', index=False)

    print("Preprocessed data saved as CSV files.")

# Run when called directly
if __name__ == "__main__":
    preprocess_data()
