import time
import pandas as pd
import numpy as np

# File names mapped to city names
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get city
    while True:
        city = input("Enter city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city. Please try again.")

    # Get month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Enter month (january to june) or 'all': ").lower()
        if month in months:
            break
        else:
            print("Invalid month. Please try again.")

    # Get day
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Enter day of week (e.g., monday) or 'all': ").lower()
        if day in days:
            break
        else:
            print("Invalid day. Please try again.")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract time components
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month
    if month != 'all':
        df = df[df['month'] == month]

    # Filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    print("\nCalculating The Most Frequent Times of Travel...\n")
    print("Most Common Month:", df['month'].mode()[0].title())
    print("Most Common Day of Week:", df['day_of_week'].mode()[0].title())
    print("Most Common Start Hour:", df['hour'].mode()[0])

def station_stats(df):
    print("\nCalculating The Most Popular Stations and Trip...\n")
    print("Most Common Start Station:", df['Start Station'].mode()[0])
    print("Most Common End Station:", df['End Station'].mode()[0])

    df['trip'] = df['Start Station'] + " to " + df['End Station']
    print("Most Common Trip:", df['trip'].mode()[0])

def trip_duration_stats(df):
    print("\nCalculating Trip Duration...\n")
    print("Total Travel Time:", df['Trip Duration'].sum(), "seconds")
    print("Average Travel Time:", round(df['Trip Duration'].mean(), 1), "seconds")

def user_stats(df):
    print("\nCalculating User Stats...\n")
    print("User Types:\n", df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print("\nGender Counts:\n", df['Gender'].value_counts(dropna=False))

    if 'Birth Year' in df.columns:
        print("\nEarliest Birth Year:", int(df['Birth Year'].min()))
        print("Most Recent Birth Year:", int(df['Birth Year'].max()))
        print("Most Common Birth Year:", int(df['Birth Year'].mode()[0]))

def display_data(df):
    """Displays 5 rows of data upon user request, continues until user says 'no' or data ends."""
    start_loc = 0
    while True:
        view_data = input('\nWould you like to see 5 rows of individual trip data? Enter yes or no: ').lower()
        if view_data != 'yes':
            break
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        if start_loc >= len(df):
            print("You've reached the end of the data.")
            break

def main():
    city, month, day = get_filters()
    df = load_data(city, month,day)

    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    display_data(df)

if __name__ == "__main__":
    main()
