import pandas as pd
import datetime

def get_data_parse_dt(week_nums):
    '''
    Function to get data and parse datetimes from MTA website. 

    Parameters: Takes a list of dates in DDMMYY format.
    '''
    url = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_{}.txt"
    dfs = []
    for week_num in week_nums:
        file_url = url.format(week_num)
        dfs.append(pd.read_csv(file_url, parse_dates=[['DATE','TIME']], keep_date_col=True))
    return pd.concat(dfs)


def parse_dt(df):
    '''
    Function to parse datetimes for the MTA df.

    Parameters: Takes MTA-format df.
    '''
    df["DATE_TIME"] = pd.to_datetime(df.DATE + " " + df.TIME, format="%m/%d/%Y %H:%M:%S")

    return df

def remove_dupes(df):
    '''
    Function to remove duplicates from the MTA df.

    Parameters: Takes MTA-format df.
    '''
    df.sort_values(["C/A", "UNIT", "SCP", "STATION", "DATE_TIME"], 
                          inplace=True, ascending=False)
    df.drop_duplicates(subset=["C/A", "UNIT", "SCP", "STATION", "DATE_TIME"], inplace=True)


def get_daily_entries(row, max_counter):
    '''
    Function to parse 'DAILY_ENTRIES' row in MTA-format df. 

    Parameters: Takes 'ENTRIES' column in series format
    '''
    
    counter = row["ENTRIES"] - row["PREV_ENTRIES"]
    if counter < 0:
        # Maybe counter is reversed?
        counter = -counter
    if counter > max_counter:
        # Maybe counter was reset to 0? 
        # print(row["ENTRIES"], row["PREV_ENTRIES"])
        counter = min(row["ENTRIES"], row["PREV_ENTRIES"])
    if counter > max_counter:
        # Check it again to make sure we're not still giving a counter that's too big
        return 0
    return counter

def get_daily_exits(row, max_counter):
    '''
    Function to parse 'DAILY_EXITS' row in MTA-format df. 

    Parameters: Takes 'EXITS' column in series format
    '''
    
    counter = row["EXITS"] - row["PREV_EXITS"]
    if counter < 0:
        # Maybe counter is reversed?
        counter = -counter
    if counter > max_counter:
        # Maybe counter was reset to 0? 
        #print(row["EXITS"], row["PREV_EXITS"])
        counter = min(row["EXITS"], row["PREV_EXITS"])
    if counter > max_counter:
        # Check it again to make sure we're not still giving a counter that's too big
        return 0
    return counter