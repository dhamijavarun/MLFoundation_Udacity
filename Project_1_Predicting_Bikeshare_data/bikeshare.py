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
    print('Welcome to the United States Bike share data portal.\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter the city you wish to see the data for: ").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("Kindly select from Chicago, New York City or Washington\n" )
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nEnter the month you wish to see the data for, all for ever month: ").lower()
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print("Kindly select all for all months or either of january, february, march, april, may or june")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nEnter the day you wish to see the data for, all for the complete week: ").lower()
        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print("Choose from either all for complete week or any day of the week")
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
    # load data file into a dataframe
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

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
    popular_month = df['month'].mode()[0]
    if popular_month == 1:
        popular_month = "January"
    elif popular_month == 2:
        popular_month = "February"
    elif popular_month == 3:
        popular_month = "March"
    elif popular_month == 4:
        popular_month = "April"
    elif popular_month == 5:
        popular_month = "May"
    else:
        popular_month = "June"
    print("The most common month is: ", popular_month)
    
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day is: ", popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common hour is: ", popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most popular origin station is: ", popular_start_station)
    
    # TO DO: display most commonly used end station
    popular_start_station = df['End Station'].mode()[0]
    print("The most popular destination station is: ", popular_start_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    station_combination = df["Start Station"].astype(str) + " to " + df["End Station"].astype(str)
    most_popular_trip = station_combination.describe()["top"]
    print("The most frequent combination of start station and end station trip is: ", most_popular_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is:", total_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time is:", mean_travel_time)
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Total number of user types: \n", user_types)
    print('-'*40)
        
    if 'Gender' and 'Birth Year' in df.columns:
        # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        print("Gender Count: \n", gender_count)
        print('-'*40)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]

        print("The earliest year of birth is: ", earliest_year)
        print("The most recent year of birth is: ", most_recent_year)
        print("The most common year of birth is: ", most_common_year)
    else:
        print("Gender Count: None")
        print("Customer birth data is not available for Washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def individual_trip_data(df):
    '''Displays the data for eachn individual trip taken for specified filters'''
    
    start = 0
    end = 5
    
    #Ask user if they want to see the individual trip data
    #and display the first five records for the same
    while True:
        user_response = input("\nWould you like to see the individiual trip data? Enter Yes or No\n").lower()
        if user_response == 'yes':
            trip_data = df[df.columns[0:-1]].iloc[start:end].to_json(orient = 'records', lines = True)[0:-1].replace('},{', '}\n{')
            print(trip_data)
            #Ask user if they want to see more trip data
            #and display the next five records and so on
            further_response = ''
            while further_response != 'no':
                further_response = input("\nWould you like to see more? Enter Yes or No\n").lower()
                if further_response == 'yes':
                    start += 5 
                    end += 5
                    trip_data = df[df.columns[0:-1]].iloc[start:end].to_json(orient = 'records', lines = True)[0:-1].replace('},{', '}\n{')
                    print(trip_data)
                elif further_response == 'no': 
                    break
                else:
                   print("Invalid input. Kindly enter Yes or No")
                   continue
            break
        elif user_response == 'no':
            break
        else:
            print("Invalid input. Kindly enter Yes or No")
            continue
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_trip_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram Interrupted. Kindly restart the application.\n')