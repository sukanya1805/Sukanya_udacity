import csv as df
import pandas as pd
import numpy as np
import time
from datetime import datetime


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
       city_filename = Chicago
    
    elif strcity.capitalize() == 'Washington':
         print("Oh it's " +strcity+ " Let's go further")
         city_filename = Washington
       
    elif strcity.capitalize() == 'New York':
         print("Oh it's " +strcity+ " Let's go further")
         city_filename = new_york_city
       
    else:
         print("Enter valid city as mentioned in the option")

# Load csv file data
    df = pd.read_csv(city_filename)
# convert the Start Time and End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    city_file = strcity.capitalize()
    return df,city_file
   
city_input_data()

def filter_raw_data(df):

   
  '''Asks the user for a time period and filter the basic processed data according 
        to the specified filter and returns the filtered data and the filter name.
    Args:
        (obj) basic processed data
    Returns:
        (obj) filtered data
        (str) Name of the filter(none, name of month, or name of the weekday).
  '''

  time_period = input('\nWould you like to filter the data by month ,day ,both or none at'
                   'all? Type "none" for no time filter\n ')
  

  if time_period == 'month':
     month_list = ('january','february','march','april','may','june')
     while True:
       get_month = (input('\nWhich month? january, february, march, april, may or june\n'))
       if get_month in month_list:
          #month_data = month_list[index(get_month)-1]
          #index = int(df['Start Time'].dt.month.mode())
          #filtered_city_data = month_list[index-1]
          filtered_city_data = df[df['month'].dt.month == month_data]
          time_period = get_month
          break
       print('Enter valid month name provided in the above options')
      
  elif time_period =='day':
        list_weekdays = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
        while True:
            #ask for the weekday of choice
            get_day = int(input('\nWhich day? Please type your response as an integer. E.g. Monday:0, Tuesday:1...\n'))
            if get_day in np.arange(0,6,1,'int'):
                #filter the data accourding to the get_day
                filtered_city_data = df[df['Start Time'].dt.dayofweek == get_day]
                time_period = list_weekdays[get_day]
                break
            print('Enter a valid day for the month:')

  elif time_period == 'both':
     month_list =('january','february','march','april','may','june')
     list_weekdays = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
     while True:
        get_month = input('Which month? january,february,march,april,may or june')
        if get_month in month_list:
         month_data = month_list.index(get_month)+1
         filtered_city_data = df[df['Start Time'].dt.month == month_data]
         time_period = get_month
         break
        print('Enter valid month name provided in the above options')
      
        get_day = int(input('\nWhich day? Please type your response as an integer. E.g. Monday:0, Tuesday:1...\n'))
        if get_day in np.arange(0,6,1,'int'):
                #filter the data accourding to the get_day
                filtered_city_data = df[df['Start Time'].dt.dayofweek == get_day]
                time_period=list_weekdays[get_day]
                break
                print('Enter a valid day for the month:')  

  else:
        filtered_city_data = df #for none option
      
  return  filtered_city_data,time_period

   
filter_raw_data(df)


