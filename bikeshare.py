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
        try:
            city = str(input('\n Please, Could you choose one of the cities (Chicago, New york city, Washington): ').lower())

    # TO DO: get user input for month (all, january, february, ... , june)
            month = str(input('\n Please, Could you choose a month from January to June: ').lower())

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = str(input('\n Please, Could you choose a weekday: ').lower())
            break

        except KeyError:
            print('\n Something went wrong. Please try again')
        except ValueError:
            print('\n Something went wrong. Please try again')


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('the most common month: {}'.format(common_month))


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('the most common day: {}'.format(common_day))


    # TO DO: display the most common start hour
    df['start_hour'] = pd.to_datetime(df['Start Time']).dt.hour
    common_start_hour = df['start_hour'].mode()[0]
    print('the most common start hour: {}'.format(common_start_hour))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(' most commonly used start station: {}'.format(common_start_station))


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\n most commonly used end station: {}'.format(common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    start = df['Start Station'].mode()[0]
    end = df['End Station'].mode()[0]
    print('\n most frequent combination of \n start station is: {} \n and end station is: {} \n '.format(start,end))




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('total travel time = {} sec'.format(round(total_travel,1)))


    # TO DO: display mean travel time
    avg_travel = df['Trip Duration'].mean()
    print('mean travel time = {} sec'.format(round(avg_travel,1)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_types(df):
    """Displays user types (subscibe & customer) on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types:\n{}'.format(user_types))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print('\ncounts of gender:\n{}'.format(gender))


    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year'].min()
    print('\n Earliest: {}'.format(int(birth_year)))

    birth_year = df['Birth Year'].max()
    print('\n Recent: {}'.format(int(birth_year)))

    birth_year = df['Birth Year'].mode()[0]
    print('\n most common year of birth: {}'.format(int(birth_year)))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_raw_data(df):
    """ display_raw_data on bikeshare raw data"""

    i = 0
    raw = input("\nWould like to see the raw data, Enter yes or no\n ").lower() # convert the user input to lower case using lower() function
    pd.set_option('display.max_rows',2)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            i += 2
            print(df[:i]) # to display next two rows
            raw = input('\nWould like to see the raw data, Enter yes or no\n ').lower() # convert the user input to lower case using lower() function
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_types(df)
        if city != 'washington':
            user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
