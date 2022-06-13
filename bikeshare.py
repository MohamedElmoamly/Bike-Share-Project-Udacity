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
    city = input('Would you like to see data for chicago, new york city, or washington? ').lower()
    while city not in(CITY_DATA.keys()):
        print('You provided invalid city name')
        
    filter = input('Would you like to filter the data by month, day, both, or none? ').lower()
    while filter not in (['month', 'day', 'both', 'none']):
        print('You provided invalid city name')

    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if filter == 'month' or filter == 'both':
        month = input('Which month - January, February, March, April, May or June? ').lower()
        while month not in months:
            print('You provided invalid month')

    else:
        month = 'all'

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Staurday', 'Sunday']
    if filter == 'day' or filter == 'both':
        day = input('which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').title()
        while day not in days:
            print('You provided invalid day')

    else:
        day = 'all'
    
    
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
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    #convert the start time column to datatime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #extract month and day of week from start time to creat new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    #filter by month if applicable
    if month != 'all':
        #use the index of the month list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        #filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    #filter by day of week if applicable
    if day != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df

def display_raw_data(df):
    """"
    Displays subsequent rows of data according to user answer
    Args: 
        df - Pandas DataFrame containing city data filtered by month and day returned from load_data() function
    """
    j = 0
    user_descion = input ("Dear sir , whould you like to see raw data or not , please answer yes or no:- ").lower()
    pd.set_option ("display.max_columns", None)   #Displays the default number of value.  upper limit to display.
    while True :
        if user_descion == "no" :
            break 
        print (df.iloc[j:(j+5)])
        user_descion = input("Dear sir , whould you like to see raw data or not , please answer yes or no:- ").lower()
        j = j+1

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

        
    #display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print(f'The most common month is: {months[month-1]}')
    
    #display the most common day of week
    day = df['day_of_week'].mode()[0]
    print(f'the most common day of week is: {day}')
    
    #display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'The most common start hour is: {popular_hour}') 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    #display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'The most popular start station is: {popular_start_station}')
    
    #display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'The most popular end station is: {popular_end_station}')
    
    #display most frequent combination of start station and end station trip
    popular_trip = df['Start Station'] + ' to ' + df['End Station'] 
    print(f'The most popular trip : from {popular_trip.mode()[0]}')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)


    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    print(df['User Type'].value_counts())


    #Display counts of gender
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts())
    else:
        print('sorry this dataset has no gender data')

        
    #Display earliest year of birth
    if 'Birth Year' in(df.columns):
        Earliest_year = int(df['Birth Year'].min())
        print("Earliest birth year is:", Earliest_year)
        
    #Display most recent year of birth     
    if 'Birth Year' in(df.columns):
        Most_recent_year = int(df['Birth Year'].max())
        print("Most recent birth year is:", Most_recent_year)
        
    #Display most common year of birth
    if 'Birth Year' in(df.columns):
        Most_Common_year = int(df['Birth Year'].mode())
        print("Most common birth year is:", Most_Common_year)
          
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    """Displays whole data required or restart."""

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
