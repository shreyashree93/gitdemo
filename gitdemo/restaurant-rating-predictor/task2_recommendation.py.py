import pandas as pd

def run():
    df = pd.read_csv('data/restaurant_data.csv')
    df.dropna(subset=['Cuisines'], inplace=True)

    user_preference = input("🍽️ Enter a preferred cuisine (e.g., Italian): ").lower()

    recommendations = df[df['Cuisines'].str.lower().str.contains(user_preference)]

    print(f"\n🍴 Top Matches for '{user_preference}':")
    print(recommendations[['Restaurant Name', 'Cuisines', 'Aggregate rating']].head(5))
