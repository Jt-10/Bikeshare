import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (int) month - month number to filter by (i.e. jan = 1, feb = 2, etc),
            or 0 for 'all' to apply no month filter
        (str) day - name of the day of week to filter by,
            or 'all' to apply no day filter
    """
    print("\nHello! Let's explore some US bikeshare data!")
    # define error message for user input error handling
    input_error = "\nI'm sorry. That didn't seem to be one of the options."

    # CITY: get user input for city (chicago, new york city, or washington)
    # reference global CITY_DATA dict
    # use a while loop to handle invalid input
    while True:
        city = input("\nWhich city's bikeshare data would you like to view:\n"
                     "Chicago, New York City, or Washington? ").lower()
        if city not in CITY_DATA:
        # looks through dict keys
            print(input_error)
        else:
            break

    # MONTH: get user input for month (all, january, february, ... , june)
    # define dict to convert between user input (str) and dt.month (int)
    # use a while loop to handle invalid input
    months = {'all': 0, 'january': 1, 'february': 2, 'march': 3, 'april': 4,
    'may': 5, 'june': 6}
    while True:
        month = input('\nWould you like to see bikeshare data for an individual\n'
                      'month (January, February, March, April, May, or June) or\n'
                      'for all months (all?) ').lower()
        if month not in months:
            print(input_error)
        else:
            # reassign to corresponding (int) value in months dict
            month = months[month]
            break

    # DAY: get user input for day of week (all, monday, tuesday, ... sunday)
    # define list of days and use a while loop to handle invalid input
    days = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday']
    while True:
        day = input('\nWould you like to see bikeshare data for a specific day\n'
                    'of the week (Monday, Tuesday, Wednesday, Thursday,\n'
                    'Friday, Saturday, or Sunday) or for all days (all)? ').title()
        if day not in days:
            print(input_error)
        else:
            break

    print('-'*60)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (int) month - month number to filter by (i.e. jan = 1, feb = 2, etc),
            or 0 for 'all' to apply no month filter
        (str) day - name of the day of week to filter by,
            or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load *.csv corresponding to city. Convert Start Time to datetime format
    # and create new columns for Month and Day of Week.
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name

    # Filter for month
    if month != 0:
        df = df[df['Month'] == month]

    # Filter for day
    if day != 'All':
        df = df[df['Day of Week'] == day]

    return df

def calc_time(start_time):
    """
    Helper function to calculate a function run time

    Args:
        (time) start time for function
    Prints:
        (time) function run time in seconds (rounded to thousandths of a sec)
    """
    print("\nThis took %s seconds." % round((time.time() - start_time), 3))
    print('-'*60)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month, day of week, and start hour
    # and create new column for Hour
    columns = ['Month', 'Day of Week', 'Hour']
    df['Hour'] = df['Start Time'].dt.hour

    for column in columns:
        print('Most common ' + column.lower() + ': ',
            df[column].mode()[0])

    calc_time(start_time)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip Combinations...\n')
    start_time = time.time()

    # display most commonly used start station, end station, and
    # trip combination and create new column for 'Trip'
    columns = ['Start Station', 'End Station', 'Trip']
    df['Trip'] = df['Start Station'] + " ----> " + df['End Station']

    for column in columns:
        print('Most commonly used ' + column.lower() + ': ',
            df[column].mode()[0])

    calc_time(start_time)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total and mean travel time in hours ('Trip Duration' is in secs)
    print('Total travel time for all trips in hours: ',
        format(int(df['Trip Duration'].sum()/360), ','))

    print('Mean travel time per trip in hours: ',
        round(df['Trip Duration'].mean()/360, 2))

    calc_time(start_time)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display percentage of user types
    print('User Type Breakdown (%):\n')
    print(df['User Type'].value_counts(normalize=True))

    # Display percentage of male/female users
    # Washington is missing gender and birth year data; capture exception
    # by using try/except statement
    try:
        print('\nUser Gender Breakdown (%) and Birth Year:\n')
        print(df['Gender'].value_counts(normalize=True))

        # Display earliest, most recent, and most common year of birth
        print('\nEarliest birth year: ', int(df['Birth Year'].min()))
        print('Most recent birth year: ', int(df['Birth Year'].max()))
        print('Most common birth year: ', int(df['Birth Year'].mode()[0]))
    except KeyError:
        print('Gender and birth year data are not available for Washington.')

    calc_time(start_time)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes' and restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
