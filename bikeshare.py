import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze ==> done
        (str) month - name of the month to filter by, or "all" to apply no month filter ==> done
        (str) day - name of the day of week to filter by, or "all" to apply no day filter ==> done
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input(
        'enter the city name you want to explore its data bikeshare ex:(chicago, new york city, washington): ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input(
            ' please\nenter the city name you want to explore its data bikeshare correct ex:(chicago, new york city, washington): ').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input(
        'enter the month name you want to explore its data bikeshare ex:(all, january, february, ... , june) : ').lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']:
        month = input(
            ' please\nenter the month name you want to explore its data bikeshare correct ex:(all, january, february, ... , june): ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(
        'enter the day name you want to explore its data bikeshare (all, monday, tuesday, ... sunday) : ').lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input(
            'please\nenter the day name you want to explore its data bikeshare correct ex:(all, monday, tuesday, ... sunday): ').lower()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze ==> done
        (str) month - name of the month to filter by, or "all" to apply no month filter ==> done
        (str) day - name of the day of week to filter by, or "all" to apply no day filter ==> done
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(
        "D:\\Projects\\python project\\bike analyize(udacity)\workspace\workspace\\new_york_city.csv")
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # print(df.head())
    df['week day'] = df['Start Time'].dt.weekday
    df['month'] = df['Start Time'].dt.month
    if day != "all":
        days = ['all', 'monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)+1
        df = df[df['week day'] == day]
        # print('',df['week day'].head())

    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june',
                  'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month)+1
        df = df[df['month'] == month]

        # print('',df['month'].head())

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common day of week
    print('the most common day of week:', df['week day'].mode()[0])
    # TO DO: display the most common month
    print('the most common month:', df['month'].mode()[0])
    # TO DO: display the most common start hour
    print('the most common start hour:', df['Start Time'].dt.hour.mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(' most commonly used start station:', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('most commonly used end station:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['start end station'] = df['Start Station']+'and'+df['End Station']
    print('most frequent combination of start station and end station trip:',
          df['start end station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time:", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('mean travel time:', df['Trip Duration'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df:
        print('counts of user types:',
              df['User Type'].value_counts().to_frame())
    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('counts of gender:', df['Gender'].value_counts().to_frame())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("most common year of birth : ", df['Birth Year'].mode()[0])
        print("most common earliest year of birth : ", df['Birth Year'].min())
        print("most common recent year of birth : ", df['Birth Year'].max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
#         code to test all options
        # day = ['all', 'monday', 'tuesday', 'wednesday',
        #        'thursday', 'friday', 'saturday', 'sunday']
        # month = ['all', 'january', 'february', 'march', 'april', 'may', 'june',
        #          'july', 'august', 'september', 'october', 'november', 'december']
        # city = ['chicago', 'new york city', 'washington']
        # for c in city:
        #     for m in month:
        #
        #         for d in day:
        #             df = load_data(c, m, d)
        #         time_stats(df)
        #         station_stats(df)
        #         trip_duration_stats(df)
        #         user_stats(df)
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_row_data = input(
            'would you like to view 5 row in the data(yes or no)').lower()
        row_counter = 0
        while show_row_data == 'yes':
            print(df.iloc[row_counter:int(row_counter+5)])
            row_counter += 5
            show_row_data = input(
                'Do you wish to continue? (yes or no) : ').lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
