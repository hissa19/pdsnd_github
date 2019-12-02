import time
import pandas as pd
import numpy as np

CITY_DATA= { 'chicago' : 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv', }

def get_filters():
    """ Asks user to specify a city, month, and day to analyze.
        Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
  
    print('Hello! Let\'s see some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Enter city name:please use chicago , new york , washington \n')
    city=city.lower()
   
    while city  not in ['chicago','new york','washington']:
        city=input('wrong input,please enter correct name of city \n')
        city=city.lower()
            
    # TO DO: get user input for month
    month=input('Enter month name or all for no filter:january , february, march , april , may , june \n')
    month=month.lower()
    months=['january', 'february', 'march', 'april', 'may', 'june','all']
    while month not in  months: 
        month=input('wrong input,please enter coreect name of month \n')
        month=month.lower()
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday) 
    day=input('Enter day name or all for no filter:saturday ,sunday , monday , tuesday , wendsday , thuresday  , friday  \n')
    day=day.lower()
    while day  not in ['saturday','sunday','monday','tuesday','wendsday','thuresday','friday','all']: 
        day=input('wrong input,please enter correct name of day \n')
        day=day.lower()
        
    print('-'*30)
    return city, month, day

def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        month_last=['january', 'february', 'march', 'april', 'may', 'june']
        month =  month_last.index(month) + 1
        df = df[ df['month'] == month ]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day'] == day.title()]
    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month is',common_month)
    print('-'*40)


    # TO DO: display the most common day of week
    common_day=df['day'].mode()[0]
    print('Most common day is',common_day)
    print('-'*40)
        


    # TO DO: display the most common start hour
    common_hour=df['hour'].mode()[0]
    print('Most common hour is',common_hour)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_statrt_station=df['Start Station'].mode()[0]
    print('Most common start station is',common_statrt_station)
    
    
    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print('Most common end station is',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['common_combination'] = df['Start Station']+ " " + df['End Station']
    common_combination=df['common_combination'].mode()[0]
    print('The most common start and end station combo is:', common_combination )



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration_total = df['Trip Duration'].sum()
    print('Trip duration total is:',trip_duration_total)

    # TO DO: display mean travel time
    trip_duration_average =df['Trip Duration'].mean()
    print('Trip duration average is:',trip_duration_average)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    user_types = df['User Type'].value_counts()
    
    print('user  classified to two types: \n',user_types)
    print('-'*40)


    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print('gender classified as the following :\n',gender_types)
        print('-'*40)

        # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:   
         most_recent_year =int(df['Birth Year'].max())
         print('most recent year is:',most_recent_year)
    
         most_earliest_year = int(df['Birth Year'].min())
         print('most earlist year is:',most_earliest_year)
    
         most_common_year = int(df['Birth Year'].mode())
         print('Most common year is:',most_common_year)
    
   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_information(df):
    
    print_status=input('do you want to print rows :yse or no \n').lower()
    
    while print_status  not in ['yes' ,'no']: 
        print_status=input('wrong input,please enter correct choice \n')
        
    if print_status == "yes":  
        prt= True 
    row=0
    while prt:
          print(df[row: row + 5])
          row = row + 5
          print_status=input('do you want to print the next 5 rows :yse or no \n').lower()
          while print_status  not in ['yes' ,'no']: 
               print_status=input('wrong input,please enter correct choice \n')
          if   print_status =='no':
             break
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_information(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

   