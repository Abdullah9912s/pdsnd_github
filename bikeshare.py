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
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("\please choose one of the following cities? new york city, chicago , washington?\n")
      if city not in ('new york city', 'chicago','washington'):
        print("oh no, please enter the city name correctly.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month =input("\nPlease choose on of the following months? january, february, march, april, may, june or all\n")
      if month not in ('january', 'february','march', 'april','may', 'june' , 'all'):
        print("please try again, enter the correct month")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day= input("\nPlease choose one of the following days (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) or all .\n")
      if day not in ('sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all'):
        print("try again, please enter the correct day")
        continue
      else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month' ] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january' , 'february' , 'march','april', 'may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week' ] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time= time.time()

    # TO DO: display the most common month
    common_month= df[ 'month' ].mode()[0]
    print('the most common month is :', common_month)

    # TO DO: display the most common day of week
    common_day =df['day_of_week'].mode()[0]
    print('the most common day is :', common_day)

    # TO DO: display the most common start hour
    df['hour' ] =df[ 'Start Time' ].dt.hour
    common_hour =df[ 'hour'].mode()[0]
    print('the most common day is :', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time= time.time()

    # TO DO: display most commonly used start station
    Starting_station= df[ 'Start Station' ].value_counts().idxmax()
    print('the most common used staring station is:', Starting_station)

    # TO DO: display most commonly used end station
    ending_Station= df['End Station' ].value_counts().idxmax()
    print('the most common ending station is:', ending_Station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_trip_station = df.groupby(['Start Station', 'End Station']).count()
    print('the most frequent combination of start and end station is:', Starting_station, " & ", ending_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('the total travel time is :', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('the mean travel time is:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time= time.time()

    # TO DO: Display counts of user types
    user_types= df[ 'User Type' ].value_counts()
    #print(user_types)
    print('the User Types is :', user_types)

    # TO DO: Display counts of gender
    try:
      gender_types= df['Gender'].value_counts()
      print('the Gender type is:', gender_types)
    except KeyError:
      print("gender types data is not available for this selections")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest_year =df['Birth Year'].min()
      print('the earliest year is:', earliest_year)
    except KeyError:
      print("earliest year data is not available for this selections")

    try:
      most_recent_year= df['Birth Year'].max()
      print('the most recent year is:', most_recent_year)
    except KeyError:
      print("recent years data is not available for this selections")

    try:
      most_common_year = df['Birth Year'].value_counts().idxmax()
      print('the most common year is:', most_common_year)
    except KeyError:
      print("common year data is not available for this selections")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    continue_ask = True
    while (continue_ask):
        print(df.iloc[0:5])
        start_loc += 5
        view_display = input('Do you want to continue ?: ').lower()
        if view_display== 'no':
            continue_ask= False

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
