import pandas as pd
import numpy as np
import datetime
import time



# Get city file names
Chicago = 'chicago.csv'
new_york_city ='new_york_city.csv'
Washington = 'washington.csv'

def city_input_data():
    '''Asks the user for a city, get the corresponding bikeshare data as Pandas
        dataframe, perform basic data processing, and 
        and returns the processed data and selected city name.
    Args:
        none.
    Returns:
        (obj) basic processed data
        (str) Name of the selected city.
    '''
   
    print("Hii all! I'm Sukanya ,Lets explore US BikeShare Data!")
    strcity = input("Would you like to see data for Chicago, New York or Washington?\n")

#strcity=strcity.capitalize()
# Conditional statement to handle invalid entries
    if strcity.capitalize() == 'Chicago':
       print("Oh it's " +strcity+ " Let's go further")
       return Chicago
       
    
    elif strcity.capitalize() == 'Washington':
         print("Oh it's " +strcity+ " Let's go further")
         return Washington
       
    elif strcity.capitalize() == 'New York':
         print("Oh it's " +strcity+ " Let's go further")
         return new_york_city
       
    else:
         print("Enter valid city as mentioned in the option")
         return city_input_data() 
    

def get_time_period(city_df):
    '''Asks the user for a time period and returns the specified filter.
    Args:
        city_df : Bikeshare dataframe
    Returns:
        (list) with two str values:
            First value: the type of filter period (i.e. month, day or none)
            Second value: the specific filter period (e.g. May, Friday)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    if time_period == 'month':
        month_list=('January', 'February', 'March', 'April', 'May', 'June')
        while True:
           month = input('\nWhich month? January, February, March, April, May, or June?\n').title()
           if month in month_list:
              city_df['month'] = city_df['Start Time'].dt.month
              month_index = month_list.index(month) + 1
              print(month_index)
              print(time_period)
              print("Statistics for month of {} " .format(month))
              city_df = city_df[city_df['month'] == month_index]
              #month_filter = city_df[city_df['Start Time'].dt.month == month_index]
              #print(month_filter)
              time_period = month
              break
           print('Enter a valid month name provided in the options')
          
    elif time_period.lower() == 'day':
         week_day_list = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
         while True:
           day_of_week = input('\nWhich day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
           if day_of_week in week_day_list:
              filtered_data = city_df[city_df['Start Time'].dt.dayofweek == day_of_week]
              time_period = day_of_week
              break
           print("\n I'm sorry, I'm not sure which day of the week you're trying to filter by. Let's try again.")
        
    else:
        filtered_data = city_df
        
    return city_df,time_period

#city_df = get_time_period(city_df)

def popular_month(city_df):
    '''Prints the popular month for the start time
    Args:
      city_df:Dataframe for bikeshare data
    Returns:
      none
    '''  
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(city_df['Start Time'].dt.month.mode())
    most_pop_month = months[index - 1]
    return most_pop_month
    print('The most popular month is {}.'.format(most_pop_month))
   
def popular_hour(city_df):
    '''Prints the popular hour of the day based on statistics
    Args:
     city_df:Bikeshare Dataframe
    Returns:
     none
    '''
    most_pop_hr = int(city_df['Start Time'].dt.hour.mode())
    print("Most Popular Hour {}".format(most_pop_hr))
    #most_pop_hr_cnt = city_df.groupby(['Start Time']).count()
    #print("Count {}".format(most_pop_hr_cnt))
    #return most_pop_hr,most_pop_hr_cnt

def popular_day(city_df):
    '''prints the most popular day of week (Monday, Tuesday, etc.) for start time.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    index = int(city_df['Start Time'].dt.dayofweek.mode())
    most_pop_day = days_of_week[index]
    print('The most popular day of week for start time is {}.'.format(most_pop_day))

#popular_day(city_df)    

def popular_station(city_df):
    '''This function returns the popular station based on Start Station and End Station
    Args:
         Bikeshare dataframe 
    '''
    pop_start_stn = city_df['Start Station'].mode().loc[0]
    #print("Popular Start Station is{}".format(pop_start_stn))
    pop_end_stn = city_df['End Station'].mode().loc[0]
    #print("Popular End Station is{}".format(pop_end_stn))
    return pop_start_stn,pop_end_stn

def popular_trip_duration(city_df):
    '''This function returns the total trip duration
    Args:
       Bikeshare dataframe  
    '''
    
    total_trip_dur = city_df['Trip Duration'].sum()
    minute ,second = divmod(total_trip_dur ,60) #60 seconds in an minute
    hr , minute = divmod(minute ,60) #60 minutes in an hour
    days ,hr = divmod(hr ,24) #24 hrs in a day
    print(" The total trip duration in {} days in {} hours , {} minutes and {} seconds" .format(days,hr,minute,second))
    #return total_trip_dur,avg_trip_dur

    
def users(city_df):
    '''This function returns the count of each user type
    Args:
        city_df: dataframe of bikeshare data
    Returns:
        (pandas series) where the index of each row is the user type and the value
            is how many trips that user type made
    '''
    user_types = city_df['User Type'].value_counts()
    return user_types
    
    
#city_df = users(city_df)

def gender(city_df):
    '''This function returns the count of gender M/F
    Args:
        city_df: dataframe of bikeshare data
    Returns:
        (pandas series) where the index of each row is the user type and the value
            is how many trips that user type made
    '''
    
    gender_count = city_df['Gender'].value_counts()
    return gender_count

#gender(city_df)

def birth_year(city_df):
    '''This funtion calculates the minimum birth year ,maximum birth year
       and popular birth year based on the occurrences  
    Args:
      city_df: dataframe of bikeshare date 
    Returns:
         None
    '''

    earliest_birth_yr = int(city_df['Birth Year'].min())
    latest_birth_yr = int(city_df['Birth Year'].max())
    print(" Earliest birth year :{} \n Latest birth year :{} " .format(earliest_birth_yr,latest_birth_yr))
          
def restart(city_df):
    '''Displays the data based on what the user specidies
        If 'yes' then further statistics is calculated else 'no'
        execution stops there
     Args:
         city_df: dataframe of bikeshare data
      Returns:
             None
     '''
    
    display = input("\n Would you like to view individual trip data?Type 'Yes/Y' or 'No/N'")
    if display =='Yes' or display == 'Y':
          statistics()
          print(city_df.head())
    elif display == 'No' or display == 'N':
          return
    else:
         print("Please enter valid option..Yes(Y) or No(N)")
         return restart(city_df)
                    
#restart(city_df)
    
def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.
    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = city_input_data()
    city_df = pd.read_csv(city)
    
   
    # parse datetime and column names
    city_df['Start Time'] = pd.to_datetime(city_df['Start Time'])
    city_df['End Time'] = pd.to_datetime(city_df['End Time'])
    start_time = time.time()

    
    # Filter data by month,day or none
    city_df,time_period = get_time_period(city_df)
    #df_filter = get_time_period(city_df)
    
    print("Loading...the data")
    print("Calculating Statistics...")
    
    print(time_period)
    if time_period == 'none':
         df_filter = city_df
         start_time = time.time()
         

    month_list = ('January', 'February', 'March', 'April', 'May', 'June') 
    if time_period in month_list:
          start_time = time.time()

          popular_month(city_df)
          print("BREAK DOWN FOR POPULAR MONTH")
          print(popular_month(city_df))
          print("That took %s seconds.\n" % (time.time() - start_time))
          print("\n Calculating the next statistic...")



    if time_period == 'day':
           popular_day(city_df) 
           print("That took %s seconds." % (time.time() - start_time))
           print("\nCalculating the next statistic...")    
           start_time = time.time()
           

        
    # Filter user type
    print("\n BREAK DOWN OF USERS----")
    print(users(city_df))
    print("That took %s seconds." % (time.time() - start_time))

    # Filter Gender
    print("\n BREAK DOWN OF GENDER----")
    print(gender(city_df))
    print("That took %s seconds." % (time.time() - start_time))

    # Filter popular hour
    print("\n BREAK DOWN FOR POPULAR HOUR")
    print(popular_hour(city_df))
    print("That took %s seconds." % (time.time() - start_time))

    # Filter birth year
    print("\n BREAK DOWN FOR POPULAR BIRTH YEAR")
    print(birth_year(city_df))
    print("That took %s seconds." % (time.time() - start_time))

    # Filter popular station  
    print("\n BREAK DOWN FOR POPULAR STATION")
    print(popular_station(city_df))
    print("That took %s seconds.\n" % (time.time() - start_time))

    # Filter Trip Duartion
    print("\n BREAK DOWN FOR TRIP DURATION")
    print(popular_trip_duration(city_df))
    print("That took %s seconds.\n" % (time.time() - start_time))

    # Restart Function
    print(restart(city_df))
    
if __name__ == "__main__":
    statistics()   
    
    
