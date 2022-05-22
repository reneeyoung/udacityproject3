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

    city = input("what city name please (chicago, new york city, washington) : ").lower()
    while city not in CITY_DATA.keys():
        print ('Please choose a valid city')
        city = input("what city name please (chicago, new york city, washington) : ").lower()         
           
#directory to store all the months
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("what month please")
        print("Month not case sensitive:\n(e.g. january or JANUARY).")
        month = input("what month please : ").lower()  
    
    if month not in MONTH_DATA.keys():
            print("\ninvalid entry, please try again")
            print("\nRestarting...")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
      
       
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

#directory to store all the days
    DAY_DATA = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7, 'all': 8}
    day = ''
    while day not in DAY_DATA.keys():
        print("which day please")
        print("Day not case sensitive:\n(e.g. monday or MONDAY).")
        day = input("what day please : ").lower()
    
    if day not in DAY_DATA.keys():
            print("\ninvalid entry, please try again")
            print("\nRestarting...")
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    
    if day != 'all':
        days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)

        # filter by month to create the new dataframe
        #df = df[df['day'] == day]

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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    common_month=months[common_month-1]
    print(f"most common month is", common_month)

    # TO DO: display the most common day of week
    common_day = df['month'].mode()[0]
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    common_day=days[common_day-1]
    print(f"most common day is", common_day)

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    common_hour=df['Start Hour'].mode()[0]
    print("most common start hour is {}:00 hrs".format(common_hour))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station= df['Start Station'].mode()[0]
    print("most common start station is {}".format(common_start_station))


    # TO DO: display most commonly used end station
    common_end_station= df['End Station'].mode()[0]
    print("most common end station is {}".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+" "+"to"+" "+ df['End Station']
    frequent_combination= df['combination'].mode()[0]
    print("most frequent combination of start station and end station is {} ".format(frequent_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    minute,second=divmod(total_travel_time,60)
    hour,minute=divmod(minute,60)
    print("total travel time: {} hours, {} minutes, and {} seconds".format(hour,minute,second))


    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    minute,second=divmod(mean_travel_time,60)
    hour,minute=divmod(minute,60)
    print("mean travel time: {} hours, {} minutes, and {} seconds".format(hour,minute,second))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts= df['User Type'].value_counts()
    print("counts of users types are:\n",user_type_counts)


    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("count of user by gender:\n", gender)
    except:
        print("no gender available")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest= int(df['Birth Year'].min())
        print("\nearliest user or oldest is from year",earliest)
    except: 
        print("no birth year available")
    
    try:
        most_recent= int(df['Birth Year'].max())
        print("most recent or youngest user is from year",most_recent)
    except: 
        print("no birth year available")
    
    try:
        most_common= int(df['Birth Year'].mode()[0])
        print("most users are born in",most_common)
    except:
        print("no birth year available")
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            view_raw_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

