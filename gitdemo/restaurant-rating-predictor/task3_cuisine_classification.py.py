import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def run():
    df = pd.read_csv('data/restaurant_data.csv')
    df.dropna(inplace=True)

    le = LabelEncoder()
    df['City'] = le.fit_transform(df['City'])
    df['Restaurant Type'] = le.fit_transform(df['Restaurant Type'])
    df['Cuisines'] = le.fit_transform(df['Cuisines'])

    X = df.drop('Cuisines', axis=1)
    y = df['Cuisines']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"🎯 Task 3 - Cuisine Classification Accuracy: {acc:.2f}")
