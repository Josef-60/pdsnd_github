import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all','january', 'february', 'march', 'april', 'may', 'june']


def check_data_entry(prompt, valid_entries):
    """
    Asks user to type some input and verify if the entry typed is valid.
    Since we have 3 inputs to ask the user in get_filters(), it is easier to write a function.
    Args:
        (str) prompt - message to display to the user
        (list) valid_entries - list of string that should be accepted
    Returns:
        (str) user_input - the user's valid input
    """
    try:
        user_input = str(input(prompt)).lower()

        while user_input not in valid_entries :
            print('Sorry... it seems like you\'re not typing a correct entry.')
            print('Let\'s try again!')
            user_input = str(input(prompt)).lower()

        print('Great! the chosen entry is: {}\n'.format(user_input))
        return user_input

    except:
        print('Seems like there is an issue with your input')

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
    city = ''
    while city not in CITY_DATA:
        city = input("Would you like to see data for Chicago, New York City or Washington ? ").lower()
    method =''
    month =''
    day =''
    # Select filter method (month, day or raw data)
    while method not in ['month', 'day', 'none']:
        method = input("Would you like to filter the data by month, day, or not at all (-> enter \'none\') ? ")

    match method:
        case 'month':
            # TO DO: get user input for month (all, january, february, ... , june)

            month = ''
            while month not in months:
                month = input("Which month do you want to see - january, february, march, april, may, june or all ? ").lower()
        case 'day':

            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            while day not in ['all','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']:
                day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all? ").title()




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
    #print(df.head())
    # convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # new columns month and weekday
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour

    if month != '' and month != 'all':
        df = df[df['month'] == months.index(month)]

     # filter by day of week if applicable
    if day != 'all' and day != '':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if not df.empty:
        most_common_month = df['month'].mode()[0]
        print("Most common month = {}".format(most_common_month))
    else:
        print("Dataframe is empty")

    # TO DO: display the most common day of week
    if not df.empty:
        most_common_day = df['day_of_week'].mode()[0]
        print("Most common day = {}".format(most_common_day))
    else:
        print("Dataframe is empty")

    # TO DO: display the most common start hour
    if not df.empty:
        most_common_hour = df['hour'].mode()[0]
        print("Most common hour = {}".format(most_common_hour))
    else:
        print("Dataframe is empty")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    if not df.empty:
        # TO DO: display most commonly used start station
        most_used_start_station = df['Start Station'].mode()[0]
        print("Most used Start Station: {}, count = {}".format(most_used_start_station,df['Start Station'].value_counts().max()))

        # TO DO: display most commonly used end station
        most_used_end_station = df['End Station'].mode()[0]
        print("Most used End Station: {}, count = {}".format(most_used_end_station,df['End Station'].value_counts().max()))


        # TO DO: display most frequent combination of start station and end station trip

        df = df[df['Start Station']==df['End Station']]

        most_freq_combination = df['Start Station'].mode()[0]
        print("Most frequent combination of start and end station: {}, count = {}".format(most_freq_combination,df['Start Station'].value_counts().max()))
    else:
        print("no data available")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (df['End Time']-df['Start Time']).sum()
    print("Total travel time = {}".format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = (df['End Time']-df['Start Time']).mean()
    print("Mean travel time = {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if not df.empty:

        # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()
        print(user_types)
        print('\n')
        # TO DO: Display counts of gender
        if 'Gender' in df:
            gender_type = df['Gender'].value_counts()
            print(gender_type)
            print('\n')
        else:
            print ("Gender not in Dataframe of {}\n".format(city.title()))
        # TO DO: Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df:
            earliest_year = int(df['Birth Year'].min())
            print("Earliest Year of birth = {}\n".format(earliest_year))

            most_recent_year = int(df['Birth Year'].max())
            print("Most recent Year of birth = {}\n".format(most_recent_year))

            most_common_year = int(df['Birth Year'].mode()[0])
            print("Most common Year of birth = {}\n".format(most_common_year))
        else:
            print("No Birth Year in Dataframe of {}".format(city.title()))
    else:
        print("no data available for user stats")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_raw_data(df):
    view =''
    print("Do you want to see raw data ?\n")
    while view != 'y' and view != 'n':
        view = input("Enter \'y\' for viewing or \'n\' to leave")
    if view == 'y':
        print(df.head())
        print('\n')
        index = 5
        cont =''
        while True:
             cont = input("continue with \'c\': ")
             if cont != 'c':
                 break
             else:
                 print(df.iloc[index:index+5])
                 index += 5


city, month, day = get_filters()
df = load_data(city, month, day)
#print(df.head())
time_stats(df)
station_stats(df)
trip_duration_stats(df)
user_stats(df)
view_raw_data(df)
