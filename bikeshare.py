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

    # Create list of user input choices
    cities = ["chicago", "new york city", "washington"]
    months = ["january", "february","march", "april", "may", "june" ,"all"]
    days = ["sunday", "monday","tuesday","wednesday","thursday","friday","saturday","all"]
    
    # create empty variables for user input
    city = " "
    month = " "
    day = " " 

   
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in cities:                                        
       user_city_input = input("Please choose a city enter chicago or new york city or washington:" )
       city = user_city_input.lower() 
        
       # if conditional to show user input error and break from while loop if input is correct 
       if city not in cities : 
           print("ERROR: please enter one of the cities choices correctly")
       else:
           break
            
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in months: 
       user_month_input = input("Which month do you wnat to filter by (january , february , march , april , may , june , all):")
       month = user_month_input.lower()
    
       if month not in months :
           print("ERROR: please enter one of the months choices correctly") 
       else:
           break
            
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)        
    while day not in days:  
       user_week_input = input("Which day do you wnat to filter by ( Sunday, Monday, Tuesday, Wednesday,Thursday, Friday, Saturday, all):")
       day = user_week_input.lower()
       
       if day not in days :
           print("ERROR: please enter one of the days choices correctly") 
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
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime( df["Start Time"])
    
    # extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["days"] = df["Start Time"].dt.weekday_name
    
    # filter by month
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        
        # filter by month to create the new dataframe
        df = df[df["month"] == month]
        
    # filter by day                         
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["days"] == day.title()]                        
                        
            
    return df


def raw_data(df):
    """ show the raw data according to user input """
    
    # create empty variables for user input 
    user_input = " "
    next_row = 0
    
    # while loop for invalid input 
    while user_input not in ["yes","no"]:
        user_input = input("Would you like to see raw data (yes or no)? :").lower()
        
        if user_input not in ["yes","no"]:
            print("ERROR:please enter valid input")
       
        elif user_input == "yes":
            print(df.head())
                      
    # while loop to iterate throuth data     
    while user_input == "yes" :
        user = input("Would you like to see next five raw data (yes or no)? :").lower()
         
        if user not in ["yes","no"]:
            print("ERROR:please enter valid input")
            
        elif user == "yes":
            next_row = next_row + 5
            print(df.iloc[next_row:next_row + 5])
            
        elif user == "no":
            break
            
                
def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #if conditional to show month data only if user input == "all"
    if month == "all":
        common_month = df["month"].mode()[0]
        print("Most frequent month: ",common_month)
    
    
    # TO DO: display the most common day
    #if conditional to show day data only if user input == "all"
    if day == "all":
        common_day = df["days"].mode()[0]
        print("Most frequent day: ",common_day)


    # TO DO: display the most common start hour
    # create an hour column from the Start Time column
    df["hour"] =df["Start Time"].dt.hour

    # find the most common hour 
    popular_hour = df["hour"].mode()[0]
    print("Most Frequent Start Hour:", popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("Most common start station: ",common_start_station)

    
    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("Most common end station: ",common_end_station)

    
    # TO DO: display most frequent combination of start station and end station trip
    df["route"] = df["Start Station"]+df["End Station"]
    print("Most common route: ",df["route"].mode()[0])
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travel time: ",round(total_travel_time),"seconds")

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Average travel time: ",round(mean_travel_time),"seconds")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df["User Type"].value_counts()
    print("The total count of each users types: ",user_types_counts )
    
    # if conditional to show gender and birth data if user input == "chicago" or "new york city"
    if city == "chicago" or city == "new york city":
        
        # TO DO: Display counts of gender
        gender_count = df["Gender"].value_counts()    
        print("The total count of each gender: ",gender_count)
        
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df["Birth Year"].min()
        print("most oldest year of birth: ",int(earliest_birth))
        recent_birth = df["Birth Year"].max()
        print("Most recent year of birth: ",int(recent_birth))
        common_birth = df["Birth Year"].mode()[0]
        print("Most common year of birth: ",int(common_birth))
    
                  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        raw_data(df)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        # create empty variables for user input
        restart = " "
        
        # while loop for invalid user input
        while restart not in ["yes","no"]:
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
            
            if restart not in ["yes","no"]:
                print("ERROR:please enter yes or no correctly")
              
        if restart != 'yes':
            break
        

if __name__ == "__main__":
	main()
