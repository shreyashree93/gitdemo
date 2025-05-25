import pandas as pd

def run():
    df = pd.read_csv('data/restaurant_data.csv')
    df.dropna(subset=['City', 'Aggregate rating'], inplace=True)

    avg_rating = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)
    print("\n🌍 Task 4 - Average Ratings by City:")
    print(avg_rating.head(5))
